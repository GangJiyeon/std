#include <stdio.h>
int count = 0;
void inc();
int get();

int main(){
    inc();
    inc();
    printf("get=%d\n", get());
    inc();
    printf("get=%d\n", get());
    return 0;
}

void inc(){
    count++;
}

int get(){
    static int last = 0;
    int diff = count - last;
    last = count;
    return diff;
}