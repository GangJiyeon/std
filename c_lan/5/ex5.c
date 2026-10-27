#include <stdio.h>
int main()
{
    int num = 0;
    printf("정수를 입력하세요");
    scanf("%d", &num);

    printf("입력한 정수 : %d\n", num);

    int count = 0;  

    while(num != 0){
        num = num / 10;
        count++;
    }
    

    printf("자리수는 %d\n", count);


    return 0;
}