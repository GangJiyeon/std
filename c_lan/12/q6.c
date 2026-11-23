#include <stdio.h>
struct pr{
    char id;
    int age;
};

int main(){
    struct pr a[5] = {
        {'A', 30}, {'B', 22}, {'C', 41},
        {'D', 19}, {'E', 27}
    };

    struct pr tmp;
    int i = 0, j = 0, min = 0;
    min = i;
    for(j = i + 1; j < 5; j++){
        if(a[j].age < a[min].age){
            min = j;
        }
    }

    tmp = a[i];
    a[i] = a[min];
    a[min] = tmp;

    for(i = 0; i < 5; i++){
        printf("%c%d ", a[i].id, a[i].age);
    }

    return 0;
}