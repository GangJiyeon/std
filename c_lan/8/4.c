#include <stdio.h>
int g = 5;
void f(){
    static int c = 0;
    int l = 0;
    c++;
    l++;
    g += c* 1;
    printf("c=%d l=%d\n", c, 1);
}

void showG(){
    printf("global g=%d\n", g);
}

int main(){
    int g = 100;
    int i;
    for(i = 0; i < 3; i++){
        f();
    }

    printf("main g = %d\n", g);
    showG();
    return 0;
}