### Exercício 3
'''
Escreva um programa que leia um número N (obrigatoriamente entre 0 e 50) e em seguida leia N números reais
em uma lista A. Exiba a lista na tela, um elemento por linha.
'''

print('Digite um valor entre 0 e 50')
N = int(input('    >> '))

while N < 0 or N > 50:
    print('    Valor inválido')
    N = int(input('    >> '))

cont = 0
lista = []
print(f'\nDigite {N} valores para uma lista: ')
while cont < N:
    lista.append(input('    >> '))
    cont += 1

print('\nElementos da lista:')
for item in lista:
    print(item)