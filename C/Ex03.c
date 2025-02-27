#include <stdio.h>
#define PI 3.1415
int main(){
	//Atividade 3
    
    float raio, perimetro, area;
    printf("Digite o raio do circulo: ");
    scanf("%f", &raio);
    perimetro = 2 * PI * raio;
    area = PI * (raio * raio);
    printf("Area do circulo: %.2f", area);
    printf("\nPerimetro do circulo: %.2f", perimetro);
    
    return 0;
}