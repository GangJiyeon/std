#include <stdio.h>
int main()
{
    int count, price, total;
    printf("상품 개수를 입력하세요 => ");
    scanf("%d", &count);

    printf("상품 단가를 입력하세요 => ");
    scanf("%d", &price);


    printf("\n 총금액 금액: %d원", price * count);

    if(count >= 20){
        printf("\n 할인율: 20%%");
        total = price * count * 0.8;
    }else if(count >= 10){
        printf("\n 할인율: 10%%");
        total = price * count * 0.9;
    }else{
        printf("\n 할인율: 0%%");
        total = price * count;
    }

    printf("\n 최종금액 금액: %d원", total);


    return 0;
}