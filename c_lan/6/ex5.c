#include <stdio.h>
#include <math.h>
int add(int a, int b)
{
    return a + b;
}

int mul(int a, int b){
    return a * b;
}

int main()
{
    printf("결과 = %d\n", add(mul(3, 4), 5));
    return 0;
}

