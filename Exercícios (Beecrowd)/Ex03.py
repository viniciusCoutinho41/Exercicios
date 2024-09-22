### Exercício 3 (Beecrowd - 1064)
'''
Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos.
Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados,
com um dígito após o ponto decimal.

Entrada
    A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante.
    Pelo menos um destes números será positivo.

Saída
    O primeiro valor de saída é a quantidade de valores positivos.
    A próxima linha deve mostrar a média dos valores positivos digitados.
'''

cont = 0
pos = 0
media = 0
while cont < 6:
    num = float(input())
    
    if num > 0:
        pos += 1
        media += num
    cont+=1
    
print(f'{pos} valores positivos')
print(f'{media/pos}')