// static 변수 누적
#include <stdio.h>
int counter(){
    static int n = 0;
    n++;
    return n;
}
int accumulate(int v){
    static int total = 100;
    int local = 100;
    total += v;
    local += v;
    printf("total=%d local=%d\n", total, local);
    return total;
}
int main(){
    int i, r = 0;
    for(i = 1; i <= 3; i++){
        r += counter();
    }
    printf("r=%d\n", r);
    accumulate(5);
    accumulate(10);
    r = accumulate(counter());
    printf("r=%d\n", r);
    return 0;
}