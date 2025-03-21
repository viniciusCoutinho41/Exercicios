#include <stdio.h>

int main(){
    //Atividade 04.2
    int num;
    
    printf("Digite um valor inteiro: ");
    scanf("%d", &num);
    while (num != 0){
        printf("%d\n", num * num);
        scanf("%d", &num);
    }

    return 0;
}