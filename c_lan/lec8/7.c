#include _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main(){
    char name[50];
    printf("이름을 입력하세요: ");
    scanf("%s", name);

    printf("입력한 이름은 %s입니다\n" name);
    printf("%d", strlen(name));
    return 0;
}