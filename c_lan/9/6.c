#include <stdio.h>
int main(){
    int x = 5, cnt = 0;
    if(x++ == 5){
        cnt += 1;
        printf("A x=%d\n", x);
    }
    if(++x == 7){
        cnt += 10;
        printf("B x=%d\n", x);
    }
    if(x-- < 7){
        cnt += 100;
        printf("C x=%d\n", x);
    }
    if(--x > 5){
        cnt += 1000;
        printf("D x=%d\n", x);
    }

    printf("cnt=%d x=%d\n", cnt, x);
}