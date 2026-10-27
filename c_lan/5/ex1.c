#include <stdio.h>
int main()
{
    int i, sum = 0;
    i = 0;

    while(i <= 10){
        sum = sum + i;
        i++;
    }

    printf("1부터 %d까지의 합 = %d", i-1, sum);
    return 0;
}