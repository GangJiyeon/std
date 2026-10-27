#include <stdio.h>
int next();
int main(){

    int i;
    for(i = 0; i < 6; i++){
        printf("%d ", next());
    }

    printf("\n");

    return 0;

}

int next(){
    static int state = 0;
    static int val = 1;

    if(state == 0){
        state = 1;
        return val;
    }else{
        state = 0;
        val *= 2;
        return val;
    }
}

// 0 1 1