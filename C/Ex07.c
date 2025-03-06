#include <stdio.h>
int main(){
	//Atividade 03.3

    int faltas, media;
    char conFinal;

    printf("Informe a quantidade de faltas: ");
    scanf("%d", &faltas);
    printf("\nInfome a media: ");
    scanf("%d", &media);

    if (faltas > 5)
        conFinal = 'F';
    else{
        if (media < 6)
            conFinal = 'C';
        else if (media >= 6 && media < 7.5)
            conFinal = 'B';
        else if (media >= 7.5 && media < 9)
            conFinal = 'A';
        else
            conFinal = 'E';
    }

    printf("O conceito final é: %c", conFinal);
    return 0;
}