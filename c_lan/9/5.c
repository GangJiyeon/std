#include <stdio.h>
int main(){
    int x = 5, y, z;
    y = x++;
    printf("x=%d y=%d\n", x, y);
    z = ++x;
    printf("x=%d z=%d\n", x, z);
    y = x-- + 2;
    printf("x=%d y=%d\n", x, y);
    z = --x * 2;
    printf("x=%d z=%d\n", x, z);
    return 0;
}