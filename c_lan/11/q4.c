#include <stdio.h>
int main(){
    int a[] = {3, 8, 1, 9, 4, 7};
    int *p = &a[1];
    int *q = &a[4];
    printf("%d\n", (int)(q-p));
    printf("%d\n", *q - *p);
    printf("%d\n", *(q - 2) + *(p + 1));
    return 0;
}