#include <stdio.h>
int main(){
    char *w[3] = {"SEOUL", "BUSAN", "JEJU"};
    int i;

    for(i = 0; i < 3; i++){
        printf("%c", *(w[i] + i));
    }

    printf("\n");

    for(i = 2; i >= 0; i--){
        printf("%s", w[i] + (i % 2 + 1));
    }

    printf("\n");
    return 0;
}
