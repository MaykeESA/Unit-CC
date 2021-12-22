print('-=-' * 10)
print('Análise de suspensão de CNH ->')
print('-=-' * 10)

sexoM = sexoF = totalCNH = totalCNHLivre = 0
CNH202M = CNH202F = CNH301M = CNH301F = CNH401M = CNH401F = 0
CNH202SuspM = CNH202SuspF = CNH301SuspM = CNH301SuspF = CNH401SuspM = CNH401SuspF = 0
listaPontos = listaM = listaF = []
y = Ppior = Mcnh = Pmelhor = 0
Npior = Spior =''

print('Digite -1 no número da CNH para receber as estatística')

while True:
    nCNH = int(input('Digite o número da CNH: '))
    if nCNH == -1:
        break

    nome = str(input('Digite o seu nome: '))
    pCNH = int(input('Digite a quantidades de pontos na CNH: '))
    listaPontos.append(pCNH)
    somaPontos = sum(listaPontos)
    iGraves = int(input('Digite a quantidade de infrações graves na CNH: '))
    sexo = str(input('Digite o sexo (M (Masculino) /F (Feminino):').upper())
    if sexo == 'M':
        sexoM += 1

        listaM.append(pCNH)
        somaPontosM = sum(listaM)

        if pCNH == 20 and iGraves >= 2:
            CNH202SuspM += 1
        elif pCNH == 20 and iGraves <= 1:
            CNH202M += 1
        elif pCNH == 30 and iGraves >= 1:
            CNH301SuspM += 1
        elif pCNH == 30 and iGraves == 0:
            CNH301M += 1
        elif pCNH == 40 and iGraves >= 0:
            CNH401SuspM += 1
        cnhSuspM = CNH202SuspM + CNH301SuspM + CNH401SuspM
        cnhLivrM = CNH202M + CNH301M + CNH401M

    elif sexo == 'F':
        sexoF += 1

        listaF.append(pCNH)
        somaPontosF = sum(listaF)

        if pCNH == 20 and iGraves >= 2:
            CNH202SuspF += 1
        elif pCNH == 20 and iGraves <= 1:
            CNH202F += 1
        elif pCNH == 30 and iGraves >= 1:
            CNH301SuspF += 1
        elif pCNH == 30 and iGraves == 0:
            CNH301F += 1
        elif pCNH == 40 and iGraves >= 0:
            CNH401SuspF += 1
        cnhSuspF = CNH202SuspF + CNH301SuspF + CNH401SuspF
        cnhLivrF = CNH202F + CNH301F + CNH401F
    else:
        print('Comando não registrado!')

    print('-=-' * 10)
    if y == 0:
        Npior = nome
        Spior = sexo
        Ppior = pCNH
        Mcnh = nCNH
        Pmelhor = pCNH
    else:
        if Ppior < pCNH:
            Npior = nome
            Spior = sexo
            Ppior = pCNH
        if pCNH < Pmelhor:
            Mcnh = nCNH
            Pmelhor = pCNH
    y += 1

totalCNH = sexoM + sexoF
totalCNHLivre = cnhLivrM + cnhLivrF

print(f'a) A quantidade de condutores do sexo feminino que não tiveram a CNH suspensa: {cnhLivrF}')
print(f'b) A média da quantidade de pontos registrados de condutores do sexo feminino: {(somaPontosF / totalCNH):.2f}')
print(f'c) O percentual de condutores do sexo masculino que tiveram a CNH suspensa com 40 pontos: {(CNH401SuspM / totalCNH) * 100:.2f}%')
print(f'd) A quantidade de condutores que não tiveram CNH suspensa: {totalCNHLivre}')
print(f'e) Nome e sexo do condutor que teve a maior quantidade de pontos registrados: {Npior} / {Spior.upper()}')
print(f'f) O número da CNH do condutor que teve menor pontuação registrada: {Mcnh}')