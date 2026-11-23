#include <stdio.h>
int main(){
    int a[] = {2, 4, 6, 8, 10};
    int b[] = {1, 3, 5, 7, 9};
    int *p[2] = {a, b};
    int i, result = 0;

    for(i = 0; i < 5; i++){
        if(i % 2 == 0){
            result += *(p[0] + i);
        }else{
            result += *(p[1] + i);
        }

        if(i == 2){
            *(p[0] + i) += 3;
        }
    }

    result += *(p[0] + 2) - *(p[1] + 1);
    printf("%d\n", result);

    return 0;
}