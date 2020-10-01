#/usr/bin/env python3

import sys

if len(sys.argv) != 4:
    print(f"USAGE\t{sys.argv[0]} value key output_file")
    print(f"Exemple\n\t{sys.argv[0]} PoC{{... X .firstpart")
    print(f"\t{sys.argv[0]} ...}} X .secondpart")
    exit(1)
value = sys.argv[1]
key = ord(sys.argv[2][0])
output = sys.argv[3]

with open(output, "wb") as f:
    for i in value:
        f.write(bytes([ord(i) ^ key]))
