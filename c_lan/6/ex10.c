#include <stdio.h>
#include <math.h>
int i = 200;
void func1();
void func2();
int main()
{
    printf("i = %d\n", i);

    i = 250;
    func1();
    func2();
    return 0;
}

int j = 300;
void func1(){

    printf("i = %d, j = %d \n", i, j);
    j = 350;
}

int k = 400;
void func2(){

    int i = 500;
    printf("i = %d, j = %d, k = %d\n", i, j, k);

}
