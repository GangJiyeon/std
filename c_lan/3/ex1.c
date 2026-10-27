#include <stdio.h>
int main()
{
    int n;
    printf("숫자를 입력하세요 => ");
    scanf("%d", &n);


    if(n % 2 == 0){
        printf("\n %d은 짝수", n);
    }else{
        printf("\n %d은 홀수", n);

    }

    return 0;
}