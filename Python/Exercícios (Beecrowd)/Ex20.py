### Exercício 20 (Beecrowd - 1115)
'''
Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada
de pontos no sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence.
O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA
(nesta situação sem escrever mensagem alguma).

Entrada
    A entrada contém vários casos de teste. Cada caso de teste contém 2 valores inteiros.

Saída
    Para cada caso de teste mostre em qual quadrante do sistema cartesiano se encontra
    a coordenada lida, conforme o exemplo.
'''

X, Y = map(int, input().split())
while X != 0 and Y != 0:
    if X > 0:
        if Y > 0:
            print('primeiro')
        else:
            print('quarto')
    else:
        if Y > 0:
            print('segundo')
        else:
            print('terceiro')
    X, Y = map(int, input().split())