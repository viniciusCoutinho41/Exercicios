#include <stdio.h>

/*

Uma empresa determinou um reajuste salarial de 5% a todos os seus funcionários.
Além disso, concedeu um abono de R$ 100,00 para aqueles que recebem até R$ 750,00.
Dado o valor do salário de um funcionário, informar para quanto ele será reajustado.

*/

int main(){
    //Exercício 2
    float salario = 0;

    printf("Digite o valor do salario: ");
    scanf("%f", &salario);

    salario *= 1.05;

    if (salario < 750)
        salario += 100;
    
    printf("O salario pos reajuste eh de: %.2f", salario);
    return 0;
}