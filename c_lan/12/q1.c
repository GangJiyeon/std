#include <stdio.h>

struct book{
    char title[20];
    int pages;
    float price;
};

int main(){
    struct book b = {"Java", 450, 0};
    b.pages -= 50;
    printf("%s %d %.1f\n", b.title, b.pages, b.price);
    printf("%c\n", b.title[3]);
    return 0;
}