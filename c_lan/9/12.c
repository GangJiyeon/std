#include <stdio.h>
void swap(int a, int b){
    int t = a;
    a = b;
    b = t;
    printf("in swap: a=%d b=%d\n", a, b);
}

int change(int n){
    n = n * 2;
    return n;
}

int main(){
    int x = 3, y = 7, r;
    swap(x, y);
    printf("x=%d y=%d\n", x, y);
    r = change(x);
    printf("x=%d r=%d\n", x, r);
    x = change(x) + change(y);
    printf("x=%d\n", x);
    return 0;
}