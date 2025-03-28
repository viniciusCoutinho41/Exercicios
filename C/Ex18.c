#include <stdio.h>

int fat(int n){
	int fat = 1, i;
	if(n != 0){
		for(i = n; i > 0; i--)
			fat *= i;
		
		return fat;
	}
	return 1;
	
}

int main() {
	//Atividade 06.3
	int val;

	printf("Digite um numero inteiro: ");
	scanf("%d", &val);
	printf("\nO fatorial de %d eh: %d", val, fat(val));

	return 0;
}