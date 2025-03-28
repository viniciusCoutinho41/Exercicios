#include <stdio.h>

double max(double a, double b){
	if (a > b)
		return a;
	return b;
}

int main(){
	//Atividade 06.1
	double val1, val2;

	printf("Digite dois valores reais para comparacao: ");
	scanf("%lf %lf", &val1, &val2);
	printf("\nO maior valor eh: %.2lf", max(val1, val2));

	return 0;
}