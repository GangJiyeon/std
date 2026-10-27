#include <stdio.h>
int main()
{
    int num0;

    printf("숫자를 입력하세요 => ");
    scanf("%d", &num0);

    if(num0 % 10 == 0){
        printf("\n%d는 5의 배수이면서 짝수입니다", num0);
    }else{
        printf("\n%d는 5의 배수가 아니거나 짝수가 아닙니다", num0);
    }

    if(num0 % 5 == 0){
        if(num0 % 2 == 0)
    }else{

    }

    return 0;
}