#include <stdio.h>
int g;
static int sg;
void f(){
    static int n;
    int loc = 1;
    n += 2;
    g += n;
    sg++;
    loc += n;
    printf("n=%d loc=%d\n", n, loc);
}

int main(){
    f();
    f();
    f();
    printf("g=%d sg=%d\n", g, sg);
    return 0;
}

// 