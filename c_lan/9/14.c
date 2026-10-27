#include <stdio.h>
int sub(int a, int b){return a - b;}
void show(int a, double b){
    printf("a=%d b=%.1f\n", a, b);
}

int main(){
    int x = 10, y = 3;
    printf("%d %d\n", sub(x, y), sub(y, x));
    printf("%d\n", sub(sub(x, y), sub(y, x)));
    show(7.9, 3);
    show(y, x / 4);
    show(x / 4.0, y / 2);
    return 0;
}