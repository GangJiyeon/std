#include <stdio.h>
int main(){
    int a[5] = {1, 2, 3, 4, 5};
    int *p = a;
    int sum = 0;
    for(int i = 0; i < 5; i++){
        *(p + i) = *(p + i) * 2;
    }
    for(int i = 0; i < 5; i += 2){
        sum += a[i];
    }
    printf("%d %d\n", a[4], sum);
    return 0;
}
