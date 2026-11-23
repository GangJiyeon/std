#include <stdio.h>
int main(){
    char *s = "PROGRAMMING";
    char *p = s;
    int cnt = 0;
    while (*p != '\0'){
        if(*p == 'M' || *p == 'G'){
            cnt += (int)(p - s) % 3 + 1;
        }
        if(*p == 'R'){
            cnt--;
        }
        p++;
    }

    printf("%d %d\n", cnt, (int)(p - s));
    return 0;
}