### Exercício 1
'''
Vamos criar um jogo de adivinhação de números. São dois jogadores – o computador e o humano – e a
ideia é a seguinte: dado um intervalo fechado [Min, Max] o jogador computador sorteia (randomiza)
um número que esteja dentro no intervalo. O segundo jogador tem como desafio descobrir qual número
foi escolhido. Para isso ele deve escolher um valor e digitá-lo. O computador deve então declarar
se está certo ou errado. Se estiver certo, terminou o jogo. Se estiver errado o computador deve
informar se o número a ser adivinhado é menor ou maior que o palpite dado e o jogo continua. Ao final
é preciso verificar quantos palpites foram dados até que o valor tenha sido adivinhado também quais
foram esses palpites. Use um vetor dinâmico para armazenar os palpites. 

Requisito a ser observado
Os valores Min e Max são fornecidos pelo usuário e podem ser quaisquer valores desde que Max seja
maior que Min + 100 (Max > Min + 100). É obrigatório que o programa verifique isso e não deixe jogar
se essa condição não for satisfeita Escreva um programa para implementar esse jogo.
'''

from random import randint

print('Vinícius Coutinho de Castro\n')
print('Pedro Pessoa de Paula Lima\n')
print('Questao 1\n')

valMin = int(input('digite o valor mínimo: '))
valMax = int(input('digite o valor máximo: '))
while valMax < valMin + 100:
    valMax = int(input('digite um valor máximo pelo menos 100 acima do mínimo: '))

numSort = randint(valMin, valMax)
chutes = []
palpite = int(input('Palpite: '))
chutes.append(palpite)

while palpite != numSort:
    if palpite < numSort:
        print('errado: seu palpite deve ser maior')
    elif palpite > numSort:
        print('errado: seu palpite deve ser menor')
    palpite = int(input('Palpite: '))
    chutes.append(palpite)

print('Acertou!!!\n')
print(f'Foram {len(chutes)} palpites até você acertar')
qtd = ''
for chute in chutes:
    qtd += str(chute) + ', '

print(f'os seus palpites foram esses: {qtd}')
