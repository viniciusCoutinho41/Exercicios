### Exercício 10
'''
Escreva um programa que leia um número inteiro N e preencha uma lista com N elementos inteiros gerados
aleatoriamente entre 0 e 1000 (usar a função randint da biblioteca random). Exiba na tela a lista gerada.
Em seguida, o programa deve ler um valor X e informar se tal valor está, ou não está presente,
bem como informar a posição de X na lista. Se houver mais de uma ocorrência de X na lista informe
todas as posições. Neste exercício não é permitido usar os operadores in e not in.
Também não é permitido usar qualquer função pronta de Python.
'''

from random import randint

print('Digite um valor máximo para a lista:')
N = int(input('    >> '))
lista = []
cont = 0
nalista = False

for i in range(N):
    lista.append(randint(0, 1000))

print(f'\n{lista}')

print('\nDigite valores para verificar se está na lista (negativo para sair)')
X = int(input('    >> '))

pos = []
naLista = False
while X >= 0:
    for i in range(N):
        if X == lista[i]:
            pos.append(i)
            naLista = True
    
    if naLista == True:
        print(f'{X} está na lista nas posições: {pos}')
        naLista = False
    else:
        print(f'{X} não está na lista')
        
    pos = []
    X = int(input('    >> '))