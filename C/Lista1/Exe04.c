#include <stdio.h>

/*

Dados 3 números imprimir o maior.

*/

int main(){
    //Exercício 4
    int a, b, c;
    printf("Digite tres valores inteiros: ");
    scanf("%d %d %d", &a, &b, &c);
    if (a >= b && a >= c)
        printf("O maior eh: %d", a);
    else if (b >= a && b >= c)
        printf("O maior eh: %d", b);
    else
        printf("O maior eh: %d", c);

    return 0;
}