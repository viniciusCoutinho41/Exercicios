### Exercício 3
'''
Considere a tabela de produtos e seus dados ao lado. Essa tabela contém códigos de produtos
e seus preços unitários de venda, que podem ocorrer no Varejo ou no Atacado, a depender da
quantidade vendida. Assim, as vendas são classificadas em dois grupos: o Grupo Varejo que
contém todas as vendas em que a quantidade não ultrapassa a quantidade mínima para atacado
(QMA) e o Grupo Atacado que contém as vendas cuja quantidade é maior ou igual à QMA. Você
deve escrever um programa que tenha como entrada inicial um número inteiro que representa
o número de vendas realizadas NV, obrigatoriamente maior que zero. Em seguida deverão ser
lidos do teclado NV pares de dados de entrada que consistem em código (Cod) e quantidade
da venda (QV). Se o código não estiver na tabela deve-se emitir a mensagem “Código inválido”
e os dados entrados devem ser ignorados. O programa deverá fazer exatamente NV leituras e se
o código for inválido essa leitura será perdida. Se o código for válido, o programa deve
calcular o valor de venda definido como Preço Unitário * QV, no qual deve ser usado o Preço
Unitário adequado, conforme a quantidade vendida, QV. Se a QV for menor que a quantidade mínima
para atacado (QMA) deve-se usar o preço de varejo, caso contrário deve-se usar o preço
de atacado. Cada venda deve ser totalizada no grupo correto, Varejo ou Atacado. Ao final o
programa deve apresentar na tela, separadamente, os totais de vendas para os Grupos Varejo e
Atacado, e o valor total de vendas.
'''

print('Vinícius Coutinho de Castro\n')
print('Pedro Pessoa de Paula Lima\n')
print('Questao 3\n')

NV = int(input('Digite o número de vendas: '))
while NV <= 0:
    NV = int(input('Número de vendas deve ser maior que zero: '))

codigos =       [16, 23, 27, 34]
precoVarejo =   [14.35, 35.12, 19.35, 63.40]
precoAtacado =  [12.93, 29.85, 16.76, 58.25]
QtdAtacados =   [50, 100, 70, 40]
totalV = 0
totalA = 0
cont = 0
invalido = False

while cont < NV:
    cod, QV = map(int, input(f'venda {cont+1}: ').split())

    for item in range(len(codigos)):
        if cod == codigos[item]:
            if QV >= QtdAtacados[item]:
                totalA += QV * precoAtacado[item]
            elif QV < QtdAtacados[item]:
                totalV += QV * precoVarejo[item]
        else:
            print('valor inválido, ignorado')
    cont += 1

print(f'total de vendas do grupo varejo: R$ {totalV:.2f}')
print(f'total de vendas do grupo atacado: R$ {totalA:.2f}')
print(f'Vendas totais: R$ {totalV + totalA:.2f}')
