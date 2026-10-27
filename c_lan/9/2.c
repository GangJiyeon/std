#include <stdio.h>
int passCnt = 0;
char grade(int s){
    if(s >= 90) return 'A';
    else if (s >= 70) return 'B';
    else if (s >= 50) return 'C';
    return 'F';
}

double record(int s){
    static int total = 0;
    static int cnt = 0;
    total += s;
    cnt++;
    if(grade(s) != 'F'){
        passCnt++;
    }
    return (double)total/cnt;
}

int main(){
    int i, score;
    double avg = 0;
    for(i = 1; i <= 5; i++){
        score = i * 20 - 5;
        avg = record(score);
        printf("%d:%c %.1f\n", score, grade(score), avg);
    }

    printf("pass=%d\n", passCnt);
    return 0;
}