### Exercício 7
'''
Elaborar um programa que efetue a leitura de valores positivos inteiros até que zero ou um valor
negativo seja informado. Ao final devem ser apresentados: o maior e menor valores informados pelo
usuário, a quantidade de valores, a soma e a média de todos.
'''

val = 1
qtd = 0
maior = 0
menor = 0
soma = 0

while val > 0:
    val = int(input("Digite um valor: "))
    qtd += 1
    soma += val

    if maior == 0 or maior < val:
        maior = val

    if val > 0:
        if menor == 0 or menor > val:
            menor = val
        
if val <= 0:
    print(f"O maior valor digitado foi: {maior}")
    print(f"O menor valor digitado foi: {menor}")
    print(f"A quantidade de valores digitados foi: {qtd-1}")
    print(f"A soma dos valores digitados foi: {soma}")
    print(f"A média dos valores digitados foi: {soma/(qtd-1)}")