J'essaie de faire un challenge de ROP

imagine ce code C
```c
#include <stdio.h>

const char *flag = "OK\n";
const char *dummy = "KO\n";

void gadget(void)
{
    __asm__("ret\n\t"
            "pop %rdi\n\t" // <---- jump here
            "ret\n\t");
}

void call_this(void) { printf(dummy); }

void abuse_me(void)
{
    char buf[32];
    fgets(buf, 64, stdin);
}

int main(void)
{
    abuse_me();
    return 0;
}
```

Le but c'est de buffer overflow.
Il faut écrire sur la valur de retour de `abuse_me` pour que ca jump sur le `pop` de `gadget`. Celui-ci va pop dans `RDI`. Ce qu'on voudrait c'est `pop` `char *flag` dans `RDI`, puis que après `gagdet`, ça jump sur le `printf()`. Le premier argument de `printf` c'est `RDI`, sauf que dans `RDI` c'est `flag` (et pas `dummy` puisqu'on a pas éxécuté le `mov`). Et du coup ça print `flag`. Idéalement ça serait un `system` mais là je test.
