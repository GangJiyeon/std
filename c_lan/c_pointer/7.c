#include <stdio.h>
int main(){
    int a = 7, b = 12;
    int *big;
    if(a > b){
        big = &a;
    }
    else{
        big = &b;
    }

    *big = *big + 100;
    big = &a;
    *big = *big - b;
    printf("%d %d\n", a, b);
    return 0;
}