#include <stdio.h>
int main(){
    int a[5] = {3, 6, 9, 12, 15};
    int *p;
    int sum = 0;
    for(p = &a[4]; p > &a[0]; p -=2){
        sum += *p;
    }
    printf("%d %d\n", sum, *p);
    return 0;
}