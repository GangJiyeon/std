#include <stdio.h>
int main(){
    int a[5] = {14, 7, 23, 5, 18};
    int max = a[0], min = a[0], i;
    for (i = 1; i < 5; i++){
        if(a[i] > max) max = a[i];
        if(a[i] < min) min = a[i];
    }

    printf("max = %d min = %d diff = %d\n", max, min, max - min);
}