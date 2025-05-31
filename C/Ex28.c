#include <stdio.h>

void minimax(float v[], int n, float *a, float *b){
    *a = *b = v[0];
    for(int i = 0; i < n; i++){
        if (v[i] < *a)
            *a = v[i];
        if (v[i] > *b)
            *b = v[i];
    }
}

int main(){
    //atividade 11.2
    float vetor[5], a, b;

    printf("Digite 5 valores:\n");
    for(int i=0; i<5; i++){
        scanf("%f", &vetor[i]);
    }
    minimax(vetor, 5, &a, &b);
    printf("maior (B): %.2f", b);
    printf("\nmenor (A): %.2f", a);
}