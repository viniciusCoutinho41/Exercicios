#include <stdio.h>
#include <string.h>

int strpos(char s[], char c){
    int i = 0;
    while (s[i] != '\0'){
        if (c == s[i])
            return i+1;
        else
            i++;
    }
    return -1;
}

int main(){
    //atividade 10.3
    char frase[100], c;

    printf("Digite uma frase: ");
    fgets(frase, 100, stdin);
    printf("Digite um caractere: ");
    scanf("%c", &c);
    printf("Primeira ocorrencia de '%c' eh na posicao: %d", c, strpos(frase, c));


    return 0;
}