#include <stdio.h>
int main()
{
    int num = 0;
    printf("정수를 입력하세요");
    scanf("%d", &num);

    printf("입력한 정수 : %d\n", num);
    int i = 0;
    int isPrime = 1;

    for(i = 2; i < num; ++i){
        if(num % i == 0){
            isPrime = 0;
            break;
        }
    }

    if(isPrime)
        printf("소수입니다.\n");
    else
        printf("소수가 아닙니다.\n");

    return 0;
}