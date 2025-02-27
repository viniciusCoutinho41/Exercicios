#include <stdio.h>
int main(){
	//Atividade 4
    
    char caracter;
    printf("Digite um caracter: ");
    scanf("%c", &caracter);
    printf("\nCaractere em octal: %o", caracter);
    printf("\nCaractere em decimal: %d", caracter);
    printf("\nCaractere em hexadecimal: %x", caracter);

    return 0;
}