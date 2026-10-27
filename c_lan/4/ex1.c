#include <stdio.h>
int main()
{
    int year;
    printf("년도를 입력하세요 => ");
    scanf("%d", &year);


    if(year % 400 == 0){
        printf("\n %d은 윤년입니다", year);
    }else if(year % 4 == 0){
        if(year % 100 != 0){
            printf("\n %d은 윤년입니다", year);
        }else{
            printf("\n %d은 평년입니다", year);
        }
    }else{
        printf("\n %d은 평년입니다", year);
    }
    return 0;
}