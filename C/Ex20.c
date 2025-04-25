#include <stdio.h>

int prod(unsigned int a, unsigned int b){
	if (b == 0) return 1;
	if (b == 1) return a;
	return (a + prod(a, b - 1));
}

int main(){
	//atividade 08.2
	unsigned int a;
	unsigned int b;
	printf("\nDigite a e b:");
	scanf("%u %u", &a, &b);
	printf("\n%u multiplicado por %u: %d", a, b, prod(a, b));
	return 0;
}