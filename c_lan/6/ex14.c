#include <stdio.h>
void incr();
int main()
{
    incr();
    incr();

    return 0;
}

void incr(void){
    static int x = 0;
    x++;
    printf("%d\n", x);
}
