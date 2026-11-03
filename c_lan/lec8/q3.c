#include <stdio.h>
int main(){
    int a[5] = {5, 3, 8, 1, 4};
    int i, t;
    for (i = 0; i < 4; i++){
        if(a[i] > a[i + 1]){
            t = a[i];
            a[i] = a[i + 1];
            a[i +1 ] = t;
        }
        
    }

    for(i = 0; i < 5; i++)
        printf("%d ", a[i]);

    printf("\n");
    return 0;
}