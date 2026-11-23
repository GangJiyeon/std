#include <stdio.h>
typedef struct{
    char name[20];
    int age;
    double height;
} Person;

int main(){
    Person pn[2] = {
        {"홍길동", 25, 178.5},
        {"박문수", 20, 180.0}
    };
    for(int i = 0; i < 2; i++){
        printf("%s %d %f\n", pn[i].name, pn[i].age, pn[i].height);
    }
}