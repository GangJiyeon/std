#include <stdio.h>
int main(){
    char *w[3] = {"BANANA", "GRAPE", "LEMON"};
    printf("%s\n", w[2]);
    printf("%c\n", *w[0]);
    printf("%c\n", *(w[1] + 2));
    printf("%c\n", *(w[0] + 4));
    return 0;
}