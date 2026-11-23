#include <stdio.h>
struct stock{
    char code[4];
    int qty;
    int price;
};

int main(){
    struct stock s[3] = {
        {"A1", 10, 200}, {"B2", 0, 500},
        {"C3", 5, 100}
    };

    int i, total = 0;
    for(i = 0; i < 3; i++){
        if(s[i].qty == 0){
            s[i].qty = 20;
        }
        total += s[i].qty * s[i].price;
    }

    printf("%d\n", total);
    printf("%s %d\n", s[1].code, s[1].qty);

    return 0;
}
