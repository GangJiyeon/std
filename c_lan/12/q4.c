#include <stdio.h>
struct card{
    char suit;
    int num;
};

int main(){
    struct card d[5] = {
        {'H', 3}, {'S', 7}, {'H', 9}, 
        {'D', 2}, {'H', 5}
    };

    int i, cnt = 0, sum = 0;
    for (i = 4; i >= 0; i--){
        if(d[i].suit == 'H'){
            cnt++;
            sum += d[i].num;
        }else{
            printf("%c%d ", d[i].suit, d[i].num);
        }
    }

    printf("\n%d %d\n", cnt, sum);

    return 0;
}