#include <stdio.h>

void inv(unsigned int n){
	if(n < 10) printf("%u", n);
	if(n >=10){
		printf("%u", n % 10);
		inv(n/10);
	}
}

int main(){
	//atividade 08.3
	unsigned int n;
	printf("Digite um número inteiro: ");
	scanf("%u", &n);
	printf("\nValor invertido: ");
	inv(n);

	return 0;
}