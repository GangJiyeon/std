#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(){
    float total, basic, amount = 0;
    float fee, duty, final= 0.0;

    printf("기본요금을 입력하세요 : ");
    scanf("%f", &basic);

    printf("전기사용량(kw) 입력하세요 : ");
    scanf("%f", &amount);

    printf("kw당 사용요금을 입력하세요 : ");
    scanf("%f", &fee);
    
    total = basic + (amount * fee);
    duty = total * 0.09;

    final = total + duty;

    printf("전체 요금은 : %f 원 \n", total);
    printf("세금은 : %f 원 \n", duty);
    printf("최종 사용 요금은 : %f 원 \n", final);



    return 0;
}