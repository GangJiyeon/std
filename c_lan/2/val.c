#include <stdio.h>
int main(){
    char ch;
    int in;
    ch = in = 'A';
    printf("\nch = %c\n", ch);
    printf("in %d", in);
    ch = in = 100;
    printf("\nch = %c\n", ch);
    printf("in = %d", in);
    return 0;
}