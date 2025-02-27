### Exercício 2
'''
Escreva um programa que apresente todos os valores inteiros divisíveis por 5 situados entre um valor
mínimo e um máximo, fornecidos pelo usuário. É obrigatório que o valor máximo seja maior que o
mínimo e se isso não ocorrer, deve ser dada uma mensagem de erro ao usuário.
'''

Min = int(input('Digite um valor mínimo: '))
Max = int(input('Digite um valor máximo: '))
cont = Min + 1

if Max > Min:
    while cont < Max:
        if cont % 5 == 0:
            print(cont)
        cont += 1
else:
    while Max < Min:
        print('\nDigite um valor máximo maior que o mínimo')
        Min = int(input('Digite um valor mínimo: '))
        Max = int(input('Digite um valor máximo: '))