#include <stdio.h>
int fare(){
    static int rides = 0;
    int cost = 120;;
    rides++;
    if(rides % 3 == 0){
        cost = 0;
    }
    return cost;
}

int main(){
    int i, total = 0;
    for(i = 1; i <= 7; i++){
        total += fare();
        printf("%d ", total);
    }

    printf("\n");
    printf("%d\n", fare());
    printf("%d\n", fare());
    return 0;
}