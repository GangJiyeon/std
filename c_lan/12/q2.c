#include <stdio.h>
struct rect {
    int w;
    int h;
};

int main(){
    struct rect r1 = {3,5}, r2 = {4, 4};
    int a1 = r1.w * r1.h, a2 = r2.w * r2.h;
    struct rect big = (a1 > a2) ? r1 : r2;
    big.w++;
    printf("%d %d\n", a1, a2);
    printf("%d %d\n", big.h, big.h);
    printf("%d %d\n", r2.w, r2.h);

    return 0;

}