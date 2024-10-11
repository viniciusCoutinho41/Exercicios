### Exercício 2
'''
Escreva um programa que leia do teclado uma lista com tamanho de 10 elementos e exiba-o na tela na ordem
inversa à ordem de leitura, sendo um elemento por linha da tela.
'''

cont = 0
lista = []
print('Digite 10 elementos para a lista:')
while cont < 10:
    lista.append(input('    >> '))
    cont += 1

print('\nElementos da lista na ordem inversa: ')
for i in range(9, -1, -1):
    print(lista[i])