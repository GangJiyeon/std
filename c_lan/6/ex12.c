#include <stdio.h>
int a = 10;
int main()
{
    extern int j, k;
    printf("j = %d\n", j);
    printf("k = %d\n", k);

    return 0;
}

int j = 300;
int k = 400;
