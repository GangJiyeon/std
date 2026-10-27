#include <stdio.h>
int main(void) {

    int i, sum = 0;

    for (i = 1; i <= 6; i++) {
        sum += (i % 2 == 0) ? i : -i;
        printf("i=%d sum=%d\n", i, sum);
    }
    
    return 0;
}