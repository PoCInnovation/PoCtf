#include <stdio.h>

void call_this(void) { printf("PoC{...}\n"); }

void abuse_me(void)
{
    char buf[32];
    fgets(buf, 50, stdin);
}

void main(void) { abuse_me(); }
