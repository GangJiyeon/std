#include <stdio.h>
int main()
{
    float origin, sale, profit = 0;
    printf("원가를 입력하세요 => ");
    scanf("%f", &origin);

    printf("판매가를 입력하세요 => ");
    scanf("%f", &sale);

    profit = (sale - origin) / origin * 100;
    printf("이익률 => %f", profit);

    if(profit >= 30){
        printf("\n최상의 수익~");
    }else if(profit >= 20){
        printf("\n좋은 수익~");
    }else if(profit >= 10){
        printf("\n보통수익");
    }else{
        printf("\n저조행");
    }

    return 0;
}