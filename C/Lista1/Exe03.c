#include <stdio.h>

/*

Dados 2 números imprimi-los em ordem crescente. Ordem crescente quando um é menor ou igual ao seguinte.

*/

int main(){
    //Exercício 3
    int a, b;
    printf("Digite dois valores inteiros: ");
    scanf("%d %d", &a, &b);
    if (a <= b)
        printf("Em ordem cresente: %d %d", a, b);
    else
        printf("Em ordem cresente: %d %d", b, a);

    return 0;
}