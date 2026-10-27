#include <stdio.h>
int main(){
    int i, count = 0;
    for(i = 1; i <= 10; i++){
        count += (i % 2 == 0) && (i % 3 == 0);
        count += (i > 8) || (i < 2);
    }

    printf("count=%d\n", count);
    printf("%d %d %d\n", 5 > 3, 5 == 3, (5 > 3) + (2 > 4) + !0);
    return 0;
}
