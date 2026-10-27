#include <stdio.h>
int x = 10;
int main(){
    int i;
    printf("A: x=%d\n", x);
    {
        int x = 20;
        x += 5;
        printf("B: x=%d\n", x);
        {
            int x = 30;
            printf("C: x=%d\n", x);
        }
        printf("D: x=%d\n", x);
    }

    for(i = 0; i < 2; i++){
        int x = i * 100;
        x++;
        printf("E: x=%d\n", x);
    }
    x++;
    printf("F: x=%d\n", x);
    return 0;
}


// 0 + 0 + 1 = 1
// 1 + 1 + 2 = 3
// 