#include <stdio.h>
int main(){
    int a[5] = {8, 4, 7, 6, 9};
    int *p = &a[0];
    while(*p % 2 == 0){
        p++;
    }
    *p = *p * 10;
    *(p + 1) += *p;
    printf("%d %d \n", *p, a[3]);
    return 0;
}