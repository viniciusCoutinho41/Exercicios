#include <stdio.h>

int main(){
    //Atividade 04.5
    int n, cont, quad = 0, imp = 1;

    printf("Digite um valor: ");
    scanf("%d", &n);
    for(cont = 0; cont < n; cont++){
        quad += imp;
        imp += 2;
    }
    printf("\nQuadrado = %d", quad);

    return 0;
}