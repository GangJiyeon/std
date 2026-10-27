#include <stdio.h>
int main()
{
    printf("200 + 200");
    printf("\n");
    printf("%d", 200+200);
    printf("\n");

    printf("%d / %d = %3.1f", 100, 200, 0.5);
    printf("\n");

    char c = 'A';
    int i = 10, j = 20, k = 30;
    printf("간단한 출력 프로그램 \n");
    printf("c = %c, c의 아스키 코드값은 %d\n", c, c);
    printf("i = %d, j = %d, k = %d", i, j, k);


    return 0;
}