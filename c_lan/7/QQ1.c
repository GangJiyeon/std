#include <stdio.h>
int main(){
    int a = 17, b = 5;
    int q = a / b;
    int r = a % b;
    double d = (double)a / b;

    printf("q=%d r=%d d=%.1f\n", q, r, d);

    if(r >= 2 && q < 4){
        printf("A\n");
    }else{
        printf("B\n");
    }

    a += q * r;
    b -= r;
    printf("a=%d b=b%d\n", a, b);
    return 0;
}

