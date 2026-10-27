#include <stdio.h>
int sum(int n){
    int i, total = 0;
    for(i = 1; i <= n; i++){
        total += i;
    }

    return total;
}

int max(int a, int b){
    return (a > b) ? a : b;
}

int main(){
    printf("%d\n", sum(sum(3)));
    printf("%d\n", max(sum(4), sum(2) * 2));
    printf("%d\n", sum(max(2, 3)) + sum(1));

    return 0;
}