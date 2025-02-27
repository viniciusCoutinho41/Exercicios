### Exercício 3
'''
Escreva um programa que leia um número inteiro N e em seguida leia N números reais, calculando a
soma de todos os valores digitados.
'''

N = int(input("Digite um número inteiro: "))
R = 0
Cont = 0
SomaR = 0
while Cont < N:
    R = float(input("Digite um número real: "))
    SomaR += R
    Cont += 1

print("A soma dos números reais é:", SomaR)