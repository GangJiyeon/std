#include <stdio.h>
int main()
{
    int year;
    printf("출생년도를 입력하세요 => ");
    scanf("%d", &year);

    switch(year % 12){
        case 0: printf("원숭이");
            break;
        case 1: printf("닭");
            break;
        case 2: printf("개");
            break;
        case 3: printf("돼지");
            break;
        case 4: printf("쥐");
            break;
        case 5: printf("소");
            break;
        case 6: printf("호랑이");
            break;
        case 7: printf("토끼");
            break;
        case 8: printf("용");
            break;
        case 9: printf("뱀");
            break;
        case 10: printf("말");
            break;
        default: printf("양");
            break;    
    }
    printf("띠 입니다\n");

    return 0;
}