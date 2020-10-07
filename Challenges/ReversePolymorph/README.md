# Reversing Polymorphic files from [WhiteComet](https://github.com/PoCInnovation/Whitecomet-Research)

## Vault (easy)

This is an x64 ELF

### Subject - for students

Polymorphism based on sections.

Find the encryption key in the ELF sections.

Flag format: `PoC{key}`

`key` is 17 bytes long. It must be submitted in base 16.

### Solve

From the subject, we know it's a polymorphic file based on sections.  
So let's check the sections: We find the section `PoC_key`  
Let's type `objdump -s -j .PoC_key Vault`

```
Contents of section .PoC_key:
 4040c0 bf7a03f6 dbe73cd5 bf8d9427 9a451042  .z....<....'.E.B
 4040d0 8b000000 00000000 00000000 00000000  ................
```

**`Flag: PoC{bf7a03f6dbe73cd5bf8d94279a4510428b}`**  
Flag regex: `PoC{bf7a03f6.*dbe73cd5.*bf8d9427.*9a451042.*8b}`

### Explanation

At each execution, the file generates a new key.

However, for this beginner challenge, the key generation is fixed.  
The point is just to show that a file can change itself.

***

## Robbery (harder)

This is an x64 ELF

### Subject - for students

Find the real instruction at offset `401ad1`.

Flag format: `PoC{ins}`

`ins` is the instruction and it's operand(s), as seen in a disassambler.

**hint 1**
This instruction is found in a malicious function.

### Solve

If we analyse the code at offset 401ad1, we see a function `decode_and_crypt`.  
If we run the code step by step, we see it's changing itself.

It's actually decoding the payload function.  
If we dissasemble payload(), it's encoded.

We must put a breakpoint in decode_and_crypt().  
Then we can jump on, or dissasemble the payload function.

Other way to solve: decode the function yourself:  
From the previous exercice, we know the where to find the encryption key.  
We can see it's a XOR, so juste XOR the function with the key.

**`Flag: PoC{call_0x4011a0_<socket@plt>}`**  
Flag regex: `PoC{call.*0x4011a0.*<socket@plt>}`


### Explanation

On execution, the binary decodes the payload in memory.

However, for this beginner challenge, the payload is never called.  
The point is to show that a file can decode a payload in memory and execute malicious code (code that could not be seen during static analysis).

Key generation is random.
