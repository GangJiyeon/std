#include <stdio.h>
#include <math.h>
void func1();

int main()
{
    int i = 0, j = 10;
    printf("i = %d, j = %d \n", i, j);

    for(i = 0; i < 2; i++){
        int i = 20;
        printf("i = %d, j = %d \n", i, j);
        func1();
    }
    return 0;
}

void func1(){
    int i = 50;
    printf("i(func1) = %d\n", i++);
}
