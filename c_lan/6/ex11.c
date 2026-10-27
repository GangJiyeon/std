#include <stdio.h>
int a = 10;
int main()
{
    int a = 20;
    {
        int a = 30;
        printf("%d\n", a);
    }

    printf("%d\n", a);
}
