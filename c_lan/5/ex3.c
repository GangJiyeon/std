#include <stdio.h>
int main()
{
    int num = 0;
    printf("정수를 입력하세요");
    scanf("%d", &num);

    printf("입력한 정수 : %d\n", num);
    int i = 0;
    for(i = 1; i <= num; ++i){
        if(num % i == 0){
            printf("%d ", i);
        }
    
    }

    return 0;
}