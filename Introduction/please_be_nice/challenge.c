#include <stdio.h>

void call_this(void) { puts("PoC{ex01}"); }

void abuse_me(void)
{
    char buf[32];
    puts("Please be nice");
    fgets(buf, 50, stdin);
}

int main(void)
{
    abuse_me();
    puts("Is that it ?");
}
