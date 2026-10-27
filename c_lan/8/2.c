#include <stdio.h>
int next(int x){
    if(x % 2 == 0){
        return x / 2;
    }
    return x * 3 + 1;
}

int main(){
    int n = 6, steps = 0;
    printf("%d", n);

    while(n != 1){
        n = next(n);
        printf(" %d", n);
        steps++;
    }

    printf("\nsteps=%d\n", steps);
    return 0;
}