### Exercício 7
'''
Escreva um programa que leia três números reais A, B e C que são os coeficientes de uma equação do
2º grau (A.x2 + B.x + C = 0). Calcule e apresente na tela as raízes dessa equação, considerando os três
casos possíveis: Delta maior que zero (duas raízes reais), Delta igual a zero (uma raiz) e
Delta menor que zero (não há raízes reais).
'''

A = float(input("digite o primeiro número real: "))
B = float(input("digite o segundo número real: "))
C = float(input("digite o terceiro número real: "))
delta = (B**2 - 4 * A * C)

if delta > 0:
    X1 = (-B + delta**0.5)/(2 * A)
    X2 = (-B - delta**0.5)/(2 * A)
    print(f"Delta positivo, duas raizes possíveis\nx1 = {X1}\nx2 = {X2}")
elif delta == 0:
    X1 = (-B + delta**0.5)/(2 * A)
    print(f"Delta igula a zero, uma raiz possível\nx = {X1}")
else:
    print("Delta negativo, não há raizes possíveis")