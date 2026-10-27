#include <stdio.h>
int main()
{
    int n;
    printf("n = ?");
    scanf("%d", &n);

    printf("\n n %% 5 = %d\n", n % 5);

    switch(n % 5){
        case 0: printf("나머지는 0\n");
            break;
        case 1: printf("나머지는 1\n");
            break;
        case 2: printf("나머지는 2\n");
            break;
        default: printf("나머지는 3이나 4\n");
            break;    
    }

    return 0;
}