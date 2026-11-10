#include <stdio.h>
int main(){
    char s[] = "ABCDE";
    int a[3] = {100, 200, 300};
    char *c = &s[0];
    int *ip = &a[0];

    c += 2;
    ip += 2;
    printf("%c %d\n", *c, *ip);
    c--;
    ip--;;
    printf("%c %d\n", *c, *ip);
    printf("%c %d\n", *(c + 1), *(ip + 1));
    return 0;
}