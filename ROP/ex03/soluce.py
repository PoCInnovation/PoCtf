#!/usr/bin/env python3

from pwn import *

elf = ELF("./challenge", checksec=False)

print(elf.symbols)
