#include <stdio.h>
int x = 5;
int f(int a);
int main()
{
    int x = 10; 
    printf("A: %d\n", f(x));
    printf("b: %d\n", x);
    x = f(x);
    printf("c: %d\n", x);
    printf("d: %d\n", x + f(1));
    return 0;
}

int f(int a){
    x += a;
    return x;
}
