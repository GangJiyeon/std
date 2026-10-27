#include <stdio.h>
int main(){
    int s;
    for(s = 95; s >= 55; s -= 20){
        printf("%d:", s);
        if(s >= 60)
            printf("D ");
        else if(s >= 80)
            printf("B ");
        else
            printf("F ");

        if(s >= 80){
            printf("B\n");
        }
        else if(s >= 60){
            printf("D\n");
        }
        else{
            printf("F\n");
        }
    }

    return 0;
}