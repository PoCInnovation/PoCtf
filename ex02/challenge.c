#include <stdio.h>

const char *flag = "PoC{ex02}\n";

void gadget(void)
{
    __asm__("ret\n"
            "pop %rdi\n\t"
            "ret\n\t");
}

void call_this(void) { printf("How did you get here ?\n"); }

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
