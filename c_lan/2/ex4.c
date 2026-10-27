#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(){
    int money_500, money_100, money_50, money_10 = 0;
    int total;

    printf("교환할 돈은? ");
    scanf("%d", &total);

    money_500 = total / 500;
    total = total % 500;

    money_100 = total / 100;
    total = total % 100;

    money_50 = total / 50;
    total = total % 50;

    money_10 = total / 10;
    total = total % 10;

    printf("오백원짜리 ==> %d개 \n", money_500);
    printf("백원짜리 ==> %d개 \n", money_100);
    printf("오십원짜리 ==> %d개 \n", money_50);
    printf("십원짜리 ==> %d개 \n", money_10);
    printf("바꾸지 못한 잔돈 ==> %d \n", total);


    return 0;
}