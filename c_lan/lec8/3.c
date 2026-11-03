#include <stdio.h>
int main(){
    int x[] = {1, 2, 3, 4};
    int y[] = {10, 20, 30, 40};
    int i, z[4], sum_z;

    for(i = 0; i < 4; i++){
        z[i] = x[i] + y[3-i];
        
    }

    printf("반대 위치의 배열요소 합\n");
    for(i = 0; i < 4; ++i){
        printf(" %d + %d = %d\n", x[i], y[3-i], z[i]);
        sum_z += z[i];
    }

    printf(" sum = %d\n", sum_z);

    return 0;
}