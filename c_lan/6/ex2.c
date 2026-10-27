#include <stdio.h>
#include <math.h>
int f();
int h();
int g();

int main()
{
   int result;
   result = f();
   printf("결과 = %d\n", result);
    return 0;
}

int f(){
    int a, b;
    a = g();
    b = h();
    return a + b;
}

int g(){
    int x = 10;
    return x * 2;
}

int h(){
    int y = 5;
    return y * 3;
}