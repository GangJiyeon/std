#include <stdio.h>
#include <math.h>
int func(int x)
{
    return x * 2;
}

int main()
{
    int a = 5;
    printf("결과 = %d\n", func(func(a)));
    return 0;
}

