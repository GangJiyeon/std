#include <stdio.h>
#include <string.h>

int main(){
    char s[11] = "hello";
    strcat(s, "world");
    printf("%s \n", s);
    return 0;
}