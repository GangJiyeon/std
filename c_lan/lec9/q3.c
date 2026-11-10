#include <stdio.h>
int main(){
    int a = 1, b = 2, c = 3;
    int *p = &a;
    *p = *p + 10;
    p = &b;
    *p = *p * 2;
    p = &c;
    *p += a;
    printf("%d %d %d %d\n", a, b, c, *p);
    return 0;
}