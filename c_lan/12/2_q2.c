#include <stdio.h>
struct pt{
    int x;
    int y;
};

int main(){
    struct pt a = {1, 5}, b = {4, 3};
    int sa = a.x + a.y, sb = b.x * b.y;
    struct pt t = (sa >= sb) ? a : b;
    t.y--;

    printf("%d %d\n", sa, sb);
    printf("%d %d\n", t.x, t.y);
    printf("%d %d\n", b.x, b.y);
    return 0;
}