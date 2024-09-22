### Exercício 6
'''
Elaborar um programa que apresente o somatório dos valores pares existentes na faixa entre 1 e N,
onde N é um número digitado pelo usuário e que deve ser no mínimo 100 (obrigatório garantir esse
requisito).
'''

maximo = int(input("Soma dos pares até: "))
minimo = 1
soma = 0

while maximo < 100:
        print("Digite um número maior que 100")
        maximo = int(input("Soma dos pares até: "))
while minimo < maximo:
    if minimo % 2 == 0:
        soma += minimo
    minimo += 1
print(f"A soma dos pares é: {soma}")