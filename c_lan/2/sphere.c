#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define PI 3.141592

int main()
{
    int radius = 0;
    float volume, area = 0.0;

    printf("구의 반지름을 입력하세요 : ");
    scanf("%d", &radius);
    
    volume = 4 / 3.0 * PI * radius * radius * radius;
    area = 4 * PI * radius * radius;

    printf("\n구의 부피는: %f", volume);
    printf("\n구의 겉넓이는: %f \n", area);
    return 0;
}