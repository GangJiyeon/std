#include <stdio.h>
int main()
{
    int a[10] = {12, 3, 19, 6, 18, 8, 12, 4, 1, 19};
    int min, i;
    min = a[0];

    for(i = 0; i < 10; i++){
        if(a[i] < min){
            min = a[i];
        }
    }
    
    printf("최소값은 %d입니다.\n", min);
    return 0;
}