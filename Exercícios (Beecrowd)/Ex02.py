### Exercício 2 (Beecrowd - 1060)
'''
Faça um programa que leia 6 valores. 
Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). 
A seguir, mostre a quantidade de valores positivos digitados.

Entrada
    Seis valores, negativos e/ou positivos.

Saída
    Imprima uma mensagem dizendo quantos valores positivos foram lidos.
'''

cont = 0
pos = 0
while cont < 6:
    num = float(input())
    
    if num > 0:
        pos += 1
    cont+=1
    
print(f'{pos} valores positivos')