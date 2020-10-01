#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

char *flag;
char key;

void gogo(void)
{
    __asm__(
            "mov [ r14 ], r15;"
            "ret;"
            "pop r14;"
            "ret;"
            "pop rdi;"
            "mov rdi, [ rdi ];"
            "ret;"
            );
}

void first_part(void)
{
    int fd = open(".firstpart", O_RDONLY);
    char buff[10];

    if (fd == -1)
        exit(1);
    if (read(fd, buff, 10) != 10)
        exit(1);
    close(fd);
    for (int i = 0; i < 10; i += 1)
        flag[i] = buff[i] ^ key;
}

void second_part(void)
{
    int fd = open(".secondpart", O_RDONLY);
    char buff[14];

    if (fd == -1)
        exit(1);
    if (read(fd, buff, 14) != 14)
        exit(1);
    close(fd);
    for (int i = 0; i < 14; i += 1)
        flag[i + 10] = buff[i] ^ key;
}

void read_inp(void)
{
    char buffer[32];

    printf("What is your name ?\n");
    read(0, buffer, 64);
    printf("your name is %s\n", buffer);
}

int main(void)
{
    setlinebuf(stdout);
    flag = calloc(25, sizeof(char));
    read_inp();
    free(flag);
    return 0;
}
