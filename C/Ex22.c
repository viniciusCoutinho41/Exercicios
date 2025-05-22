#include <stdio.h>
#define max 7

void obtem(float temp[], int dias){
	for(int i = 0; i < dias; i++){
		printf("Digite uma temperatura para o %dº dia da semana: ", i + 1);
		scanf("%f", &temp[i]);
	}
}

float media(float vet[], int tam){
	float total = 0;
	for(int i = 0; i < tam; i ++){
		total += vet[i];
	}
	return total / tam;
}

int conta(float vet[], int tam, float media){
	int acima = 0;
	for(int i = 0; i < tam; i ++){
		if (vet[i] > media){
			acima += 1;
		}
	}
	return acima;
}

int main() {
	//atividade 09.3
	float temp[max], m;
	obtem(temp, max);
	m = media(temp, max);
	printf("Estatística: %d", conta(temp, max, m) );
	return 0;
}