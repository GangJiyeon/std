#include <stdio.h>
int main(){
    char *w[3] = {"APPLE", "KIWI", "MELON"};
    printf("%s\n", w[1]);
    printf("%c\n", *w[0]);
    printf("%c\n", *(w[2] + 1));
    printf("%c\n", *(w[1] + 3));
    printf("%c\n", *w[2] + 1);
    return 0;
}