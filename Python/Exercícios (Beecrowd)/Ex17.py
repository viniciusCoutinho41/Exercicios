### Exercício 17 (Beecrowd - 1101)
'''
Leia um conjunto não determinado de pares de valores M e N
(parar quando algum dos valores for menor ou igual a zero). Para cada par lido,
mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

Entrada
    O arquivo de entrada contém um número não determinado de valores M e N.
    A última linha de entrada vai conter um número nulo ou negativo.

Saída
    Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles,
    conforme exemplo abaixo.
'''

M, N = map(int, input().split())
while N > 0 and M > 0:
    ordem = []
    numeros = ''
    if N > M:
        cont = M
        while cont <= N:
            ordem.append(cont)
            cont += 1
    else:
        cont = N
        while cont <= M:
            ordem.append(cont)
            cont += 1
    for num in ordem:
        numeros += str(f'{num} ')
    print(f'{numeros}Sum={sum(ordem)}')
    M, N = map(int, input().split())