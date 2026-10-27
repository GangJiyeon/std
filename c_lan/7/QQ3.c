#include <stdio.h>
int main(void) {

    int i, cnt = 0;

    for (i = 0; i < 5; i++) {
        switch (i % 3) {
            case 0: cnt += 1;
            case 1: cnt += 10;
                break;
            default: cnt += 100;
        }

        printf("i=%d cnt=%d\n", i, cnt);
    }
    return 0;
}