#include <stdio.h>
int fee(int type, int hours){
    int base;
    switch(type){
        case 1: base = 1000; break;
        case 2: base = 1500; break;
        default: base = 2000;
    }
    if(hours > 3){
        return base * 3 + (hours - 3) * base/ 2;
    }

    return base * hours;
}

int main(){
    int h, total = 0, f;
    for(h = 2; h <= 5; h++){
        f = fee(h % 3, h);
        total += f;
        printf("h=%d fee=%d\n", h, f);
    }
    printf("total=%d\n", total);
    return 0;
}