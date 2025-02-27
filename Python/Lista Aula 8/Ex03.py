###Exercício 3
'''
Escreva um programa que leia do teclado uma lista com tamanho de 10 elementos e exiba-a na tela na
ordem inversa à ordem de leitura.
'''

print('Digite 10 valores para a lista')
lista = []
cont = 0

while cont < 10:
    num = float(input('   >> '))
    lista.insert(0, num)
    cont += 1
print(lista)