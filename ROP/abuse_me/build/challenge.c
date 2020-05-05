#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <errno.h>

const char *flag = "flag.txt";

void print_file(char *path)
{
    char buf[100];
    FILE *fp = fopen(path, "r");

    if (fp == NULL) {
        printf("fopen: %s: %s\n", path, strerror(errno));
        exit(1);
    }
    fgets(buf, 100, fp);
    printf(buf);
}

void abuse_me(void)
{
    char buf[32];
    fgets(buf, 64, stdin);
}

void main(void)
{
    abuse_me();
    print_file("dummy.txt");
}
