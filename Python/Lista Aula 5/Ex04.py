### Exercício 4
'''
Escreva um programa que leia um número inteiro N e em seguida leia N números reais, calculando a
soma de todos os valores positivos fornecidos, ignorando os negativos.
'''

N = int(input("Digite um número inteiro: "))
R = 0
Cont = 0
SomaR = 0
while Cont < N:
    R = float(input("Digite um número real: "))
    if R > 0:
        SomaR += R
    Cont += 1

print("A soma dos números reais positivos é:", SomaR)