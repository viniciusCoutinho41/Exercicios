### Leitura do Arquivo e Separação do Conteúdo
with open('entrada.txt', 'r') as entrada:
    NPC = int(entrada.readline())

    listaE = []
    listaD = []
    for linha in entrada:
        E, D = map(int, linha.split())
        listaE.append(E)
        listaD.append(D)

### Comparação de itens da Lista
def ComparaLista(Lista, lado):
    if NPC >= 1 and NPC <= 2000:
        qtdRpt = -1
        resultados = []
        for item in Lista:
            for compara in Lista:
                if item == compara:
                    qtdRpt += 1

            if qtdRpt >= 1 and [item, lado, qtdRpt] not in resultados:
                resultados.append([item, lado, qtdRpt])
            qtdRpt = -1
        
        return resultados

### Saída
with open('saida.txt', 'w') as saida:
    resD = ComparaLista(listaD, 'D')
    resE = ComparaLista(listaE, 'E')
    resFinal = sorted(resE + resD, key=lambda item: (item[0], -ord(item[1][0])))

    if len(resFinal) == 0:
        saida.write('SEM TROCAS DESTA VEZ')
    else:
        for item in resFinal:
            saida.write(f'{item[0]} {item[1]} {item[2]}\n')