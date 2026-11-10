#include <stdio.h>
int main(){
    int a = 3, b = 7;
    int *p1 = &a, *p2 = &b;
    *p1 = *p1 + *p2;
    *p2 = *p1 - *p2;
    printf("a = %d\n", a);
    printf("b = %d\n", b);
    return 0;
}