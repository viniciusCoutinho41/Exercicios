#define PI 3.1415
int main(){
	//Atividade 1
	
	float IMC, peso, altura;
	system("cls");
	printf("Digite o peso e a altura: ");
	scanf("%f %f", &peso, &altura);
	IMC = peso/(altura * altura);
	printf("%f", IMC);
	
	return 0;
}