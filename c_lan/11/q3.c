#include <stdio.h>
int main(){
    int a[] = {5, 10, 15, 20, 25};
    int *p = a + 1;
    int x, y, z;
    x = *p + *(p + 2);
    p++;
    y = *(p + 2) - *p;
    z = *p + 2;
    printf("x = %d, y = %d, z = %d\n", x, y, z);
    return 0;
}