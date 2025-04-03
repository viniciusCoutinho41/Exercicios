#include <stdio.h>

/*

Faça um programa que receba o número de lados de um polígono convexo (N >= 3),
calcule e mostre o número de diagonais desse polígono. Sendo N o número de lados
do polígono, o número de diagonais é dado por:
ND = N(N - 3) / 2.

Obs.: O número de diagonais é sempre inteiro e caso N seja menor que 3,
solicite novo valor para N até que N seja maior ou igual a 3.

*/

int main(){
    //Exercício 1
    int numLado, diag = 0;
    do {
        printf("\nDigite o numero de lados de um poligono convexo (maior ou igual a 3): ");
        scanf("%d", &numLado);
    } while (numLado < 3);
    
    diag = numLado * (numLado - 3) / 2;
    printf("\n\nO numero de diagonais de um poligono convexo de %d lados, eh de: %d", numLado, diag);

    return 0;
}