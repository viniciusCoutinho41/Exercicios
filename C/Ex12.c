#include <stdio.h>

int main(){
    //Atividade 04.4
    int val, pot, res = 1;

    printf("\nDigite um valor real: ");
    scanf("%d", &val);

    printf("Digite um valor inteiro maior que zero: ");
    scanf("%d", &pot);

    for(pot; pot > 0; pot--){
        res *= val;
    }
    printf("\npotencia = %d", res);

    return 0;
}