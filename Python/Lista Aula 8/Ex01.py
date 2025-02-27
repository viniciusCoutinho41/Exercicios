### Exercício 1
'''
Escreva um programa que permaneça em laço até que seja digitado o valor zero ou negativo. Cada valor
positivo lido deve ser inserido no final de uma lista, usando o método append. Ao final exiba a lista
completa na tela.
'''

print('Digite um valor positivo (zero ou negativo para sair)')
num = float(input('   >> '))
lista = []

while num > 0:
    lista.append(num)
    num = float(input('   >> '))

print(lista)