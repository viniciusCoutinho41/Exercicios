#include <stdio.h>

void ord(int *a, int *b){
    int aux;
    if (*a > *b){
        aux = *a;
        *a = *b;
        *b = aux;
    }   
}

int main(){
    //atividade 11.1
    int a, b;
    printf("Digite dois valores inteiros: ");
    scanf("%d %d", &a, &b);

    ord(&a, &b);

    printf("\nMenor (A): %d", a);
    printf("\nMaior (B): %d", b);
}