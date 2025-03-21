#include <stdio.h>

int main(){
    //Atividade 04.3
    int n, fat;
    printf("Digite um valor inteiro maior que zero: ");
    scanf("%d", &n);
    fat = n;
    while(n > 1){
        fat *= (n - 1);
        n--;
    }
    printf("\nfatorial = %d", fat);

    return 0;
}