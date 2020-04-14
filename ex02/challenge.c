#include <stdio.h>

const char *flag = "PoC{ex02}\n";
const char *dummy = "How did you get here ?\n";

void gadget(void)
{
    __asm__("ret\n"
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
