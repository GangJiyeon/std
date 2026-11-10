#include <stdio.h>
int main(){
    int a[5] = {4, 9, 2, 7, 5};
    int *p = &a[0], *maxp = &a[0];
    int i, t;
    for(i = 1; i < 5; i++){
        if(*(p + i) > *maxp){
            maxp = p + i;
        }
    }
    t = *maxp;
    *maxp = *p;
    *p = t;

    printf("%d %d %d\n", a[0], a[1], (int)(maxp - p));
    return 0;
}