#include <stdio.h>
#include <math.h>
int sum(int n){
    int i;
    int total = 0;

    for(i = 1; i <= n; i++){
        total += i;
    }

    return total;
}
int main()
{
    printf("%d\n", sum(5));
    return 0;
}

