#include <stdio.h>

int main(){
    int a = 100;
    char b = 'b';
    void *p = NULL;
    p = (int*)&a;
    printf("*p = %d\n", *(int*)p);
    p = (char*)&b;
    printf("*p = %c\n", *(char*)p);
    printf("%x",p);
    return 0;
}