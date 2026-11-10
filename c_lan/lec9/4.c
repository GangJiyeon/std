#include <stdio.h>
int main(){
    
    int a = 10;
    int b = 20;
    int *p1;
    int *p2;
    
    p1 = &a;
    p2 = &b;
    *p1 = 100;
    *p2 = 200;

    printf("a = %d\n", a);
    printf("b = %d\n", b);
}