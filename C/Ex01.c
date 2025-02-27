#include <stdio.h>
int main(){
	//Atividade 1
	
	float IMC, peso, altura;
	printf("Digite o peso e a altura: ");
	scanf("%f %f", &peso, &altura);
	IMC = peso/(altura * altura);
	printf("%.2f", IMC);
	
	return 0;
}