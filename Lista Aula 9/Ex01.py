### Exercício 1
'''
Escreva um programa que leia do teclado uma lista com tamanho de 10 elementos e exiba-o na tela um elemento
por linha.
'''

cont = 0
lista = []
print('Digite 10 elementos para a lista:')
while cont < 10:
    lista.append(input('    >> '))
    cont += 1

print('\nElementos da lista: ')
for item in lista:
    print(item)