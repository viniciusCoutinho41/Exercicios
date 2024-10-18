### Exercício 9
'''
Escreva um programa que leia um número inteiro N e preencha uma lista com N elementos inteiros gerados
aleatoriamente entre 0 e 1000 (usar a função randint da biblioteca random). Exiba na tela a lista gerada.
Em seguida, o programa deve ler um valor X e informar se tal valor está, ou não está presente na lista.
Neste exercício é permitido usar os operadores in e/ou not in
'''

from random import randint

print('Digite um valor máximo para a lista:')
N = int(input('    >> '))
lista = []
cont = 0

for i in range(N):
    lista.append(randint(0, 1000))

print(f'\n{lista}')

print('\nDigite valores para verificar se está na lista (negativo para sair)')
X = int(input('    >> '))
while X >= 0:
    if X in lista:
        print(f'    {X} está na lista')
    else:
        print(f'    {X} não está na lista')
    X = int(input('    >> '))