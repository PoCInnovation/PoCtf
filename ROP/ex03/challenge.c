#include <stdio.h>
#include <stdlib.h>

char *mdr;

void gadget(void)
{
    __asm__("ret\n"
            "pop %rsi\n\t"
            "ret\n\t");
}

void do_it(char *s) { system(s); }

void call_this(int _, int arg)
{
    __asm__("pop %rdi\n\t");
    if (arg != 0xdead)
        exit(0);
}

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
