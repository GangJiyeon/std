#include <stdio.h>
int f(int x){
    printf("f(%d) ", x);
    return x * 2;
}
int g(int x){
    printf("g(%d) ", x);
    return x + 1;
}
int main(){
    int a, b, c;
    a = f(g(1));
    printf("a=%d\n", a);
    b = g(f(a));
    printf("b=%d\n", b);
    c = (a > 3 ) ? f(a) : g(a);
    printf("c = %d\n", c);

    return 0;
}