### Exercício 12 (Beecrowd - 1018)
'''
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas)
no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.
A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias,
conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha,
caso contrário seu programa apresentará a mensagem: “Presentation Error”.
'''

valor = int(input())
valorNota = valor
notaCem = 0
notaCinquenta = 0
notaVinte = 0
notaDez = 0
notaCinco = 0
notaDois = 0
moedaUm = 0
cont = 0

if valor < 1000000:
    while valorNota != 0:
        if valorNota >= 100:
            valorNota -= 100
            notaCem += 1
        elif valorNota >= 50:
            valorNota -= 50
            notaCinquenta += 1
        elif valorNota >= 20:
            valorNota -= 20
            notaVinte += 1
        elif valorNota >= 10:
            valorNota -= 10
            notaDez += 1
        elif valorNota >= 5:
            valorNota -= 5
            notaCinco += 1
        elif valorNota >= 2:
            valorNota -= 2
            notaDois += 1
        else:
            valorNota -= 1
            moedaUm += 1

print(f'{valor}')
print(f'{notaCem} nota(s) de R$ 100,00')
print(f'{notaCinquenta} nota(s) de R$ 50,00')
print(f'{notaVinte} nota(s) de R$ 20,00')
print(f'{notaDez} nota(s) de R$ 10,00')
print(f'{notaCinco} nota(s) de R$ 5,00')
print(f'{notaDois} nota(s) de R$ 2,00')
print(f'{moedaUm} nota(s) de R$ 1,00')