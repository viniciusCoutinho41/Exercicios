### Exercício 4
'''
Escreva um programa que leia um número N (obrigatoriamente entre 0 e 50) e em seguida preencha uma lista
com N elementos inteiros gerados aleatoriamente entre 0 e 1000 (usar a função randint da biblioteca random
– veja o quadro sobre isso no exercício 9).
'''

from random import randint

print('Digite um valor entre 0 e 50')
N = int(input('    >> '))

while N < 0 or N > 50:
    print('    Valor inválido')
    N = int(input('    >> '))

cont = 0
lista = []
while cont < N:
    lista.append(randint(0, 1000))
    cont += 1

print('\nElementos da lista:')
for item in lista:
    print(item)