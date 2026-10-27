#include <stdio.h>
int main()
{
    int sub1, sub2, sum = 0;

    printf("첫 번째 과목 점수를 입력하세요 => ");
    scanf("%d", &sub1);

    printf("두 번째 과목 점수를 입력하세요 => ");
    scanf("%d", &sub2);

    sum = sub1 + sub2;

    printf("두 과목의 합계: %d점", sum);
    if(sum >= 170 && sum >= 150){
        printf("\n합격~");
    }else{
        printf("\n불합격");
    }

    return 0;
}