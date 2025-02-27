### Exercício 4
'''
Reescreva um programa do exercício anterior considerando exclusivamente os números positivos
fornecidos. Caso seja digitado zero ou um valor negativo o programa deve exibir uma mensagem
"número inválido" e o valor deve ser ignorado.
'''

N = int(input('Digite um número inteiro: '))
menor = 0
maior = 0
cont = 0

while cont < N:
    R = float(input('Digite um número real: '))
    if R > 0:
        if R < menor or menor == 0:
            menor = R
        if R > maior or maior == 0:
            maior = R
    else:
        print('Número inválido')
    cont += 1

if menor == 0 and maior == 0:
    print('\nNenhum valor válido digitado')
else:
    print(f'\nO maior valor digitado foi {maior}')
    print(f'O menor valor digitado foi {menor}')