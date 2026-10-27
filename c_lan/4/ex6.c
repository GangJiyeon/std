#include <stdio.h>
int main()
{
    int a, b, c = 0;
    printf("삼각형 세 변의 길이를 입력하세요 => ");
    scanf("%d %d %d", &a, &b, &c);

    int valid = 0;

    if(a + b > c && b + c > a && a + c > b){
        printf("유효한 삼각형")
    }else{
        printf("유효하지 않은 삼각형");
    }
    return 0;
}