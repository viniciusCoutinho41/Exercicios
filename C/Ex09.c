#include <stdio.h>

int main(){
    //Atividade 04.1

    int x, y;
    x = 3;
    y = x * (x + 1) * x++;
    printf("Instrucao: y = x * (x + 1) * x++");
    printf("\nx = %d", x);
    printf("\ny = %d", y);

    x = 5;
    y = 3;
    y *= x + 1;
    printf("\n\nInstrucao: y *= x + 1");
    printf("\nx = %d", x);
    printf("\ny = %d", y);

    return 0;
}