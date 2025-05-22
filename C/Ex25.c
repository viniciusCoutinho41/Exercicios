#include <stdio.h>
#include <string.h>

int main(){
    //atividade 10.2
    char frase[100];
    int i = 0;

    printf("Digite uma frase: ");
    fgets(frase, 100, stdin);
    
    printf("\nInvertido: ");
    for(i = strlen(frase); i >= 0; i--){
        printf("%c", frase[i]);
    }

    return 0;
}