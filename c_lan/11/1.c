#include <stdio.h>
int main(){
    char *p = "COMPUTER";
    for(int i = 0; *(p + i) != '\0'; i++){
        printf("%c", *(p + i));
    }

    return 0;

}