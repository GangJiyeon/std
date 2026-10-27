#include <stdio.h>
int main()
{
    int month;
    printf("월을 입력하세요 => ");
    scanf("%d", &month);

    switch(month){
        case 2: printf("28");
            break;
        case 4: 
        case 6: 
        case 9: 
        case 11: printf("30");
            break;
        default: printf("31");
            break;    
    }
    printf("일 입니다\n");

    return 0;
}