#include <stdio.h>

int main(){
    int n = 1230, rev = 0, count = 0;
    while (n > 0){
        rev = rev * 10 + n % 10;
        n = n /10;
        count++;
    }

    printf("rev=%d count=%d n=%d\n", rev, count, n);
    return 0;
}