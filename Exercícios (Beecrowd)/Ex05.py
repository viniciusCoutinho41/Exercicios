### Exercício 5 (Beecrowd - 1066)
'''
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares,
quantos valores digitados foram ímpares, quantos valores digitados foram positivos
e quantos valores digitados foram negativos.

Entrada
    O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
    Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha,
    não esquecendo o final de linha após cada uma.
'''

cont = 0
pares = 0
impares = 0
pos = 0
neg = 0
while cont < 5:
    num = int(input())
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    cont+=1
    
print(f'{pares} valor(es) par(es)')
print(f'{impares} valor(es) impar(es)')
print(f'{pos} valor(es) positivo(s)')
print(f'{neg} valor(es) negativo(s)')
