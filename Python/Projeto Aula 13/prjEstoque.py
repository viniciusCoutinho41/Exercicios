### Leitura do arquivo PRODUTOS
with open('PRODUTOS.txt', 'r') as entProdutos:
    Produtos = []

    for linha in entProdutos:
        codProd, qtdProd, qtdMin = map(int, linha.split(sep=';'))
        Produtos.append([codProd, qtdProd, qtdMin])

### Leitura do arquivo VENDAS
with open('VENDAS.txt', 'r') as entVendas:
    Vendas = []

    for linha in entVendas:
        codVend, qtdVend, sitVend, canalVend = map(int, linha.split(sep=';'))
        Vendas.append([codVend, qtdVend, sitVend, canalVend])

# Produtos[linha][0] -> codProd
# Produtos[linha][1] -> qtdProd
# Produtos[linha][2] -> qtdMin

# Vendas[linha][0] -> codVend
# Vendas[linha][1] -> qtdVend
# Vendas[linha][2] -> sitVend
# Vendas[linha][3] -> canalVend

### Quantidade de vendas
def QtVendas():
    qtdProdVend = []
    for i in range(len(Produtos)):
        totalVend = 0
        for linha in range(len(Vendas)):
            if Produtos[i][0] == Vendas[linha][0] and Vendas[linha][2] < 103:
                totalVend += Vendas[linha][1]
        
        qtdProdVend.append([Produtos[i][0], totalVend])

    return qtdProdVend

### Estoque após vendas
def EstqAposVendas():
    qtdVendas = QtVendas()
    EstoqueFinal = []
    for i in range(len(Produtos)):
        EstoqueFinal.append([Produtos[i][0], Produtos[i][1] - qtdVendas[i][1]])

    return EstoqueFinal

### Necessidade
def Necessidade():
    EstoqueFinal = EstqAposVendas()
    Necess = []
    for i in range(len(Produtos)):
        if EstoqueFinal[i][1] < Produtos[i][2]:
            Necess.append([Produtos[i][0], Produtos[i][2] - EstoqueFinal[i][1]])
        else:
            Necess.append([Produtos[i][0], 0])

    return Necess

### Transferencia
def TransfCO():
    Necess = Necessidade()
    Transf = []
    for i in range(len(Necess)):
        if Necess[i][1] > 1 and Necess[i][1] < 10:
            Transf.append([Produtos[i][0], 10])
        else:
            Transf.append([Produtos[i][0], Necess[i][1]])
    
    return Transf

### Divergencias de Código
def DivergCod():
    DiverCod = []
    for cod in range(len(Vendas)):
        verCod = 0
        for compara in range(len(Produtos)):
            if Vendas[cod][0] == Produtos[compara][0] and verCod == 0:
                verCod += 1
        
        if verCod == 0:
            DiverCod.append([cod, Vendas[cod][0]])

    return DiverCod

### Divergencias de Situação
def DivergSit():
    DiverSitC = []
    DiverSitNF = []
    DiverSitE = []
    for i in range(len(Vendas)):
        if Vendas[i][2] == 135:
            DiverSitC.append(i)
        elif Vendas[i][2] == 190:
            DiverSitNF.append(i)
        elif Vendas[i][2] == 999:
            DiverSitE.append(i)

    return DiverSitC, DiverSitNF, DiverSitE

### Total de Vendas nos Canais
def TotalCanais():
    totalCanais = []
    for i in range(4):
        total = 0
        for item in range(len(Vendas)):
            if Vendas[item][3] == i + 1 and Vendas[item][2] < 103:
                total += Vendas[item][1]
        
        totalCanais.append(total)
    
    return totalCanais

### Saída -> Transfere
with open('TRANSFERE.txt', 'w', encoding='UTF-8') as saiTransfere:
    saiTransfere.write(f'Necessidade de Transferência Armazém para CO\n\nProduto QtCO QtMin QtVendas  Estq.após Necess.  Transf. de\n')
    saiTransfere.write(f'{'Vendas':>38} {'Arm p/ CO':>19}\n')
    
    qtdVendas = QtVendas()
    estqFinal = EstqAposVendas()
    necess = Necessidade()
    transf = TransfCO()

    for item in range(len(Produtos)):
        saiTransfere.write(f'{Produtos[item][0]} {Produtos[item][1]:6} {Produtos[item][2]:5} {qtdVendas[item][1]:8} {estqFinal[item][1]:10} {necess[item][1]:7} {transf[item][1]:11}\n')
    
### Saída -> Divergências
with open('DIVERGENCIAS.txt', 'w', encoding='UTF-8') as saiDivergencias:
    codDiv = DivergCod()
    DiverSitC, DiverSitNF, DiverSitE = DivergSit()
    Diverg = ''

    if len(codDiv) > 0:
        for i in range(len(codDiv)):
            Diverg += f'Linha {codDiv[i][0] + 1} - Código de Produto não encontrado {codDiv[i][1]}\n'
    if len(DiverSitC) > 0:
        for i in range(len(DiverSitC)):
            Diverg += f'Linha {DiverSitC[i]} - Venda cancelada\n'
    if len(DiverSitNF) > 0:
        for i in range(len(DiverSitNF)):
            Diverg += f'Linha {DiverSitNF[i]} - Venda não finalizada\n'
    if len(DiverSitE) > 0:
        for i in range(len(DiverSitE)):
            Diverg += f'Linha {DiverSitE[i]} - Erro desconhecido. Acionar equipe de TI.\n'

    saiDivergencias.write(Diverg)

### Saída -> Total de Canais
with open('TOTCANAL.txt', 'w', encoding='UTF-8') as saiTotalCanais:
    saiTotalCanais.write(f'Quantidades de Vendas por canal\n\nCanal {'':22} QtVendas\n')
    total = TotalCanais()
    for i in range(len(total)):
        match i:
            case 0:
                saiTotalCanais.write(f'1 - Representantes {total[i]:18}\n')
            case 1:
                saiTotalCanais.write(f'2 - Website {total[i]:25}\n')
            case 2:
                saiTotalCanais.write(f'3 - App móvel Android {total[i]:15}\n')
            case 3:
                saiTotalCanais.write(f'4 - App móvel iPhone {total[i]:16}')