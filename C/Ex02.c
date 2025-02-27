#include <stdio.h>
int main(){
	//Atividade 2
	
	float F, C;
    printf("Digite a temperatua em Fahrenheit: ");
    scanf("%f", &F);
    C = (F - 32) * 5/9;
    printf("%.2f", C);
    
    return 0;
}