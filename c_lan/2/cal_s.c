#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    int height, length, s = 0;
    
    
    printf("삼각형의 밑변을 입력하세요");
    scanf("%d", &length);

    printf("\n삼각형의 높이를 입력하세요");
    scanf("%d", &height);
    
    s = (int)height * length * 0.5;
    printf("\n삼각형의 넓이는 : %d \n", s);

    return 0;
}