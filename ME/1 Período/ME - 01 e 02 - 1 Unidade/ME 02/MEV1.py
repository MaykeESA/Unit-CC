print('-=-' * 20)
print('Informações sobre Corona Vírus -> ')
print('Digite "-1" no código do estado para receber as estatísticas')
print('-=-' * 20)

qtdprimeiro, menorestado, qtdmenorestado, totalEstados = 0, 0, 0, 0
listaES, listapC, listamC = [], [], []

while True:
    UF = input("Digite o código do estado (UF): ")
    if UF == '-1':
        break

    nEstado = str(input("Digite o nome do Estado: "))
    listaES.append(nEstado)
    totalEstados = totalEstados + 1

    pCorona = int(input("Digite o número de pacientes que testaram positivo para o Corona Vírus: "))
    listapC.append(pCorona)
    somaCasos = sum(listapC)

    mCorona = int(input("Digite o número de óbito recorrente ao Corona Vírus: "))
    listamC.append(mCorona)
    somaMortes = sum(listamC)
    print('-=-' * 10)

    if qtdprimeiro == 0:
        qtdprimeiro = pCorona

    if menorestado == 0:
        menorestado = nEstado
        qtdmenorestado = mCorona

    elif mCorona < qtdmenorestado:
        menorestado = nEstado
        qtdmenorestado = mCorona

    if pCorona > mCorona:
        print()
    else:
        print('O número de Mortes é maior que o pacientes que testaram positivo!')
        print('Dados inconsistente!')
        break

print(f'a) Média de pacientes infectados nos estados cadastrados: {somaCasos / totalEstados}')
print (f'b) Estado que apresenta o menor numero de obitos: {menorestado}')
print(f'c) O primeiro estado cadastrado possui {(listapC[0] / somaCasos) * 100:.2f}% dos totais de casos')