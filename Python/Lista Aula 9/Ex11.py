### Exercício 11
'''
Escreva um programa que leia um número inteiro N e preencha uma lista com N elementos inteiros gerados
aleatoriamente entre 0 e 1000. Exiba na tela a lista gerada. Em seguida, o programa deve ler um valor X e,
caso X esteja na lista, deve eliminá-lo. Caso haja várias ocorrências de X, todas devem ser eliminadas.
Pesquise como usar a função del (você vai precisar dela e neste exercício será permitido usá-la).
'''

from random import randint

print('Digite um valor máximo para a lista:')
N = int(input('    >> '))
lista = []
nalista = False

for i in range(N):
    lista.append(randint(0, 10))

print(f'\n{lista}')

print('\nDigite valores para eliminar da lista (negativo para sair)')
X = int(input('    >> '))

cont = 0
while X >= 0:
    if X in lista:
        while cont < len(lista):
            if X == lista[cont]:
                del lista[cont]
            else:
                cont += 1
        
        print(f'Valor excluído, lista atualizada:\n{lista}')
    
    cont = 0
    print('Digite o próximo valor')
    X = int(input('    >> '))