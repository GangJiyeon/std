#include <stdio.h>
#include <math.h>
int square(int x)
{
    return x * x;
}

int main()
{
    int result;
    result = square(2) + square(3);
    printf("결과 = %d\n", result);
    return 0;
}

