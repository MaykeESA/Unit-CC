print('-=-' * 10)
print('Análise de suspensão de CNH ->')
print('-=-' * 10)

qtdCNH = int(input('Digite a quantidade de CNH para análise: '))
listaPontos = []
somaPontos, cnh301, cnh202, totalCNH = 0, 0, 0, 0

for i in range(1, qtdCNH + 1, 1):
    nCNH = int(input('Digite o número da CNH: '))
    pCNH = int(input('Digite a quantidades de pontos na CNH: '))
    listaPontos.append(pCNH)
    somaPontos = sum(listaPontos)
    iGraves = int(input('Digite a quantidade de infrações graves da CNH escolhida: '))
    totalCNH += 1
    print('-=-' * 10)

    if pCNH == 30 and iGraves >= 1:
        cnh301 += 1
    if pCNH == 20 and iGraves >= 2:
        cnh202 += 1

print(f'a) A quantidade de condutores que tiveram a CNH suspensa com 30 pontos foi {cnh301}')
print(f'b) O percentual de condutores que tiveram a CNH suspensa com 20 pontos foi {(cnh202 / totalCNH) * 100:.2f}%')
print(f'c) A média de quantidade de pontos registrados foi {(somaPontos / totalCNH):.2f}')