#include <stdio.h>
int main(){
    int x, in = 0, out = 0;
    for(x = -5; x <= 105; x += 55){
        if(x < 0 || x > 100)
            out++;
        else
            in++;

        if(!(x >= 0 && x <= 100))
            printf("%d:out ", x);
        else
            printf("%d:in ", x);
    }

    printf("\nin=%d out=%d\n", in, out);

    return 0;
}

// 42 8 0 