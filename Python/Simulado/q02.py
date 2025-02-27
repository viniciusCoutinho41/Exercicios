### Exercício 2
'''
Escreva um programa que leia um número inteiro N, obrigatoriamente par e maior ou igual a 6 e
menor ou igual a 32. Se o N for ímpar ou fora da faixa [6, 32] deve ser mostrada a mensagem
“O número TAL é inválido”, onde TAL deve ser substituído pelo valor digitado. Neste caso outro
valor deve ser lido. Enquanto o usuário do programa insistir em digitar valores inválidos para
N, o programa deve permanecer lendo. Se N for válido o programa deve exibir na tela um desenho
formado por asteriscos e espaços em branco, cuja largura total seja exatamente N caracteres,
conforme exemplos abaixo. O lado esquerdo do desenho deve estar encostado no lado esquerdo da tela.
A espessura da parede deve ser de 2 asteriscos e o espaço interno montado com espaços em branco.
'''

print('Vinícius Coutinho de Castro\n')
print('Pedro Pessoa de Paula Lima\n')
print('Questao 2\n')

N = int(input('Digite um valor inteiro: '))

while N % 2 != 0 and 32 < N or N < 6:
    print(f"O número {N} é inválido")
    N = int(input('Digite um valor inteiro: '))

cont = 1
a = ' '
b = '*'
c = '*'
desenho = []

while cont < N:
    if cont != N - 1:
        a += '*'
    else:
        a += ' '
    cont += 1
desenho.append(a)

cont = 1
while cont < N:
    b += '*'
    cont += 1
desenho.append(b)

cont = 1
while cont < N:
    if cont == 1:
        c += '*'
    elif cont == N - 2:
        c += '*'
    elif cont == N - 1:
        c += '*'
    else:
        c += ' '
    cont += 1
desenho.append(c)
i = 0
linha = 0
while linha < len(desenho):
    if linha == 0:
        print(desenho[linha])
    elif linha == 1:
        print(desenho[linha])
    elif linha == 2:
        while i < N - 4:
            print(desenho[linha])
            i += 1
        print(desenho[1])
        print(desenho[0])
    linha += 1
