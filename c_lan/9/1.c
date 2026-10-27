#include <stdio.h>
int divSum(int n){
    int i, s = 0;
    for(i = 1; i < n; i++){
        if(n % i == 0){
            s += i;
        }
    }

    return s;
}

int main(){
    int n, found = 0;
    for(n = 2; n <= 30; n++){
        if(divSum(n) == n){
            printf("%d ", n);
            found++;
            
        }
    }

    printf("\nfound=%d\n", found);
    return 0;
}