#define PI 3.1415
int main(){
	//Atividade 2
	
	float F, C;
    system("cls");
    printf("Digite a temperatua em Fahrenheit: ");
    scanf("%f", &F);
    C = (F - 32) * 5/9;
    printf("%.2f", C);
    
    return 0;
}