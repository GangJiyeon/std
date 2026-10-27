#include <stdio.h>
int calc(int a, char op, int b){
    int r;

    switch(op){
        case '+': r = a + b; break;
        case '-': r = a - b; break;
        case '*': r = a * b; break;
        case '/': r = (b != 0) ? a / b : 0; break;
        case '%': r = a % b; break;
        default: r = -1;
    }

    return r;
}

int main(){

    int t;
    t = calc(7, '*', 6);
    printf("%d\n", t);
    t = calc(t, '/', 5);
    printf("%d\n", t);
    t = calc(t, '%', 3) + calc(t, '-', 10);
    printf("%d\n", t);
    t = calc(t, '/', 0) + calc(4, '^', 2);
    printf("%d\n", t);
    return 0;
}

//