#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{

    int total, sale, amount, profit, origin = 0;

    printf("판매가를 입력하세요 : ");
    scanf("%d", &sale);

    printf("원가를 입력하세요 : ");
    scanf("%d", &origin);

    printf("수량을 입력하세요 : ");
    scanf("%d", &amount);

    total = sale * amount;
    profit = (sale - origin) * amount;
    printf("\n========== 계산결과 ==========\n");
    printf("총판매액 : %d 원\n", total);
    printf("판매이익 : %d 원\n", profit);
    
    return 0;
}