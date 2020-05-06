#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## xor
## File description:
##
##

import sys

s = "baguette"
j = 0
b = bytearray(open(sys.argv[1], 'rb').read())
for i in range(len(b)):
    b[i] ^= ord(s[j])
    j += 1
    if (j == 8):
        j = 0
open(sys.argv[1], 'wb').write(b)
