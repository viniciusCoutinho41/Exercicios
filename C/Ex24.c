#include <stdio.h>
#include <string.h>

int main(){
    //atividade 10.1
    char frase[100];
    int i = 0, plvr = 0;

    printf("Digite uma frase: ");
    fgets(frase, 100, stdin);

    while(frase[i] != '\0'){
        if (frase[i] == ' '){
            plvr++;
        }
        i++;
    }

    printf("\nPalavras digitadas: %d", plvr+1);
    return 0;
}