#include <stdio.h>
#define max 10

//define a nota 1, nota 2 e média de cada aluno
void entrada(float vet[][3], int tam){
	for (int i=0; i < tam; i++){
        for (int j=0; j<2; j++){
            printf ("Aluno %d - Nota %d: ", i+1, j+1);
            scanf ("%f", &vet[i][j]); //notas
        }
        vet[i][2] = (vet[i][0] + vet[i][1])/2; //media
    }
}

//calcula a média da turma
float media(float vet[][3], int tam){
	float total = 0;
	for (int i=0; i<tam; i++){
        total += vet[i][2];
    }

	return total / tam;
}

//conta quais estão acima da média
char* conta(float vet[][3], int indice, float media){
	if(vet[indice][2] > media) return "Acima da media";
	if(vet[indice][2] < media) return "Abaixo da media";
	return "Na media";
}

int main(){
    //atividade 09.4
    float A[10][3];
	entrada(A, max);
	printf("Média da turma: %.2f", media(A, max));
	printf("\n\nMedia do Aluno\tStatus");
    for (int i=0; i<max; i++){
		printf("\n%.2f\t\t%s", A[i][2], conta(A, i, media(A, max)));
    }

    return 0;
}