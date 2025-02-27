### Exercício 4 (Beecrowd - 1065)
'''
Faça um programa que leia 5 valores inteiros.
Conte quantos destes valores digitados são pares e mostre esta informação.

Entrada
    O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
    Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.
'''

cont = 0
pares = 0
while cont < 5:
    num = int(input())
    if num % 2 == 0:
        pares += 1
    cont+=1
    
print(f'{pares} valores pares')