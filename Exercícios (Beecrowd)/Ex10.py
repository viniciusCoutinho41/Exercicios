### Exercício 10 (Beecrowd - 1094)
'''
Maria acabou de iniciar seu curso de graduação na faculdade de medicina
e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável.
Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório
e o percentual de cada tipo de cobaia utilizada.

Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos.
Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados,
o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

Entrada
    A primeira linha de entrada contém um valor inteiro N
    que indica os vários casos de teste que vem a seguir.
    Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15)
    que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'),
    indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

Saída
    Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada
    e o percentual de cada uma em relação ao total de cobaias utilizadas,
    sendo que o percentual deve ser apresentado com dois dígitos após o ponto.
'''

N = int(input())
cont = 0
totalC = 0
totalR = 0
totalS = 0

while cont < N:
    Qtd, Tipo = map(str,input().split())
    Qtd = int(Qtd)

    if Tipo == 'S':
        totalS += Qtd
    elif Tipo == 'R':
        totalR += Qtd
    elif Tipo == 'C':
        totalC += Qtd
    cont += 1

total = (totalS + totalR + totalC)
porcC = (totalC/total) * 100
porcR = (totalR/total) * 100
porcS = (totalS/total) * 100

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {totalC}')
print(f'Total de ratos: {totalR}')
print(f'Total de sapos: {totalS}')
print(f'Percentual de coelhos: {porcC:.2f} %')
print(f'Percentual de ratos: {porcR:.2f} %')
print(f'Percentual de sapos: {porcS:.2f} %')