#include <stdio.h>
int half1(int x){ return x / 2;}
double half2(int x){ return x / 2;}
double half3(double x){ return x / 2;}
int half4(double x){ return x / 2;}
int main(){
    printf("%d\n", half1(7));
    printf("%.1f\n", half2(7));
    printf("%.1f\n", half3(7));
    printf("%d\n", half4(7.0));
    printf("%d\n", half1(half1(9) + 0.9));
    printf("%.1f\n", half3(half1(9)));

    return 0;
}

