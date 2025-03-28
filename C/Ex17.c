#include <stdio.h>

void rodizio(int placa){
	
	switch(placa){
        case 1: 
        case 2: printf("Segunda-feira"); break;
        case 3: 
        case 4: printf("Terça-feira"); break;
        case 5: 
        case 6: printf("Quarta-feira"); break;
        case 7: 
        case 8: printf("Quinta-feira"); break;
        case 9: 
        case 0: printf("Sexta-feira"); break;
		default: printf("Digito invalido"); break;
    }
}

int main() {
	//Atividade 06.2
	int placa;

	printf("Digite o ultimo digito da placa de um carro (entre 0 e 9): ");
	scanf("%d", &placa);
	rodizio(placa);

	return 0;
}