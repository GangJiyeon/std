#include <stdio.h>
int main()
{
    float cm, kg, std = 0;   // std => 표준몸무게(키에따른)
    printf("실제 키(cm)를 입력하세요 : ");
    scanf("%f", &cm);

    printf("실제 몸무게(kg)를 입력하세요 : ");
    scanf("%f", &kg);


    if(cm < 150){
        std = cm - 100;
    }else if(cm <= 160){
        std = (cm - 150)/2 + 50;
    }else{
        std = (cm - 100)*0.9;
    }

 
    float obs = (kg-std)*100/std;

    printf("표준몸무게 : %f kg", std);
    printf("\n비만도 : %f", obs);

    printf("\n등급 : ");
    if(obs <= 10){
        printf("정상 ");
    }else if(obs <= 20){
        printf("과체중 ");
    }else{
        printf("비만 ");

    }

    return 0;
}