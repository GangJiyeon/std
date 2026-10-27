#include <stdio.h>
int main(){
    int x = 4, y, z;
    y = 2 * x * x + 4 * x -7;
    printf("%d\n", y);
    z = -x * x + 3 * -x -7;
    printf("%d\n", z);
    y = - -x + -(-x);
    printf("%d\n", y);
    z = 2 + 3 * 4 % 5 - 6 / 4;
    printf("%d %d\n", z, 100 / 10 / 5 * 2);
    return 0;
}