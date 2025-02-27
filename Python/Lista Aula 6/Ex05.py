### Exercício 5
'''
Escreva um programa que contenha um laço que será executado enquanto o número digitado for
diferente de zero. Para cada número digitado pelo usuário mostrar na tela apenas os que forem divisíveis
por 2 e por 3.
'''

print('Digite um valor (zero para sair)')
N = float(input('   >> '))

while N != 0:
    if N % 6 == 0:
        print(f'Valor {N} é divisível por 2 e por 3')
    N = float(input('   >> '))