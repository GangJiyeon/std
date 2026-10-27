#include <stdio.h>
int fib_next();

int main(){
    int i; 
    for(i = 0; i < 7; i++){
        printf("%d ", fib_next());
    }
    printf("\n");
    return 0;
}

int fib_next(){
    static int a = 0, b = 1;
    int cur = a;
    int next = a + b;
    a = b;
    b = next;
    return cur;
}

