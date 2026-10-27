#include <stdio.h>
#include <math.h>
int max(int a, int b)
{
    if(a > b){
        return a;
    }else{
        return b;
    }

}
int main()
{
    printf("%d\n", max(15, max(8, 20)));
    return 0;
}

