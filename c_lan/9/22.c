// 200 1000 

#include <stdio.h>
int balance = 1000, fails = 0;
int deposit(int amt) {
    static int count = 0;
    balance += amt;
    return ++count;
}
int withdraw(int amt){
    if(amt > balance){
        fails++;
        return 0;
    }
    balance -= amt;
    return 1;
}

int main(){
    int i, ok, n = 0;
    for(i = 1; i <= 5; i++){
        if(i % 2 == 1){
            n = deposit(i *200);
        }
        else{
            ok = withdraw(i * 500);
            printf("i=%d ok=%d bal=%d\n", i, ok, balance);
        }
    }

    printf("n=%d fails=%d\n", n, fails);
    printf("interest=%.1f\n", balance * 3 / 100.0);
    return 0;
}