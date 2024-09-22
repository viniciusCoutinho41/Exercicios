### Exercício 3
'''
Escreva um programa que leia um número inteiro N e em seguida leia N números reais, separando o
menor e o maior, apresentando-os na tela.
'''

N = int(input('Digite um número inteiro: '))
menor = 0
maior = 0
cont = 0

while cont < N:
    R = float(input('Digite um número real: '))
    if R < menor or menor == 0:
        menor = R
    if R > maior or maior == 0:
        maior = R
    cont += 1

print(f'\nO maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')