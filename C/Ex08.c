#include <stdio.h>
#include <math.h>
int main(){
	//Atividade 03.4
    
    int a, b, c;
    float x1, x2, delta;

    printf("Digite os valores de a, b e c, respectivamente: ");
    scanf("%d %d %d", &a, &b, &c);

    if (a != 0){
        delta = pow(b, 2) - 4 * a * c;
        if (delta > 0){
            x1 = (-b + sqrt(delta))/(2 * a);
            x2 = (-b - sqrt(delta))/(2 * a);
            printf("x1 = %.2f\nx2 = %.2f", x1, x2);
        }
        else{
            printf("Nao existem raizes reais");
        }
    }
    else{
        printf("Nao existem raizes reais");
    }

    return 0;
}