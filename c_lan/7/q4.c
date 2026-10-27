#include <stdio.h>
int gen();

int main(){
    printf("%d\n", gen());
    printf("%d\n", gen());
    printf("%d\n", gen() + gen());

    return 0;
}

int gen(){
    static int n = 0;
    return n++;
}