#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(){
    int a[5];
    int i;

    for(i=0; i<5; i++){
        printf("정수 %d개를 입력하세요: ", i+1);
        scanf("%d", &a[i]);
    }

    printf(i = 0; i < 5; i++);

    for(i = 0; i < 5; i++){
        printf("a[%d] = %d\n", i, a[i]);
    }
}