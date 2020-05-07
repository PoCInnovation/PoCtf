#include <stdio.h>

void call_this(void)
{
    char buf[100];
    FILE *fp = fopen("flag.txt", "r");

    fgets(buf, 100, fp);
    printf(buf);
}

void abuse_me(void)
{
    char buf[32];
    puts("Please be nice");
    fgets(buf, 50, stdin);
}

int main(void)
{
    setlinebuf(stdout);
    abuse_me();
    puts("Is that it ?");
}
