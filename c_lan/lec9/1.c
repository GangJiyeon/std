#include <stdio.h>
void main(){
    int days = 365;
    int month = 12;
    int *addr = 0;
    addr = &days;
    printf("days의 주소는 %x %x\n", &days, addr);
    printf("month의 주소는 %x\n", &month);
}