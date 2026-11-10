#include <stdio.h>
int main(){
    int a[4] = {2, 4, 6, 8};
    int *p = &a[0];
    int sum = 0, i;
    for(i = 0; i < 4; i++){
        sum += *p;
        p++;
    }
    printf("%d\n", sum);
    printf("%d\n", *p);
    p--;
    printf("%d\n", *p);
    return 0;
}