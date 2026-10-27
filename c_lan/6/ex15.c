#include <stdio.h>
int g = 0;
int calc(int x);
int main()
{
    int i;
    for(i = 1; i <= 3; i++){
        printf("결과 = %d\n", calc(i));
    }

    printf("g = %d\n", g);

    return 0;
}

int calc(int x){
    int a = x;
    static int s = 0;
    s += x;
    g += x;
    return a + s;
}
