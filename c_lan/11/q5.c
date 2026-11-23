#include <stdio.h>
int main(){
    int a[] = {1, 2, 3, 4};
    int b[] = {5, 6, 7, 8};
    int *PA[2];
    PA[0] = a;
    PA[1] = b;
    printf("%d\n", *(PA[1] + 2));
    printf("%d\n", *PA[0] + 3);
    printf("%d\n", *(PA[0] + 3));
    printf("%d\n", *PA[1] + *(PA[0] + 1));
    return 0;
}