#include <stdio.h>
int main(){
    char cp[] = "computer";
    int i;
    
    for(i = 0; cp[i] != '\0'; i++){
        printf("%c\n", cp[i]);
        printf("%c\n", *(cp + i));
    }

    return 0;
}