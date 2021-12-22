listaPC = []
listaNomeR = []
listaEspec = []
listaFono = []
listaNutri = []
listaFisio = []
listaOdonto = []
listaClinico = []
listaDinheiro = []
listaTotalDescConv = []
valorConsulta = 0

print('*' * 24)
print('* Clínica Saúde e Vida *')
print('*' * 24)

# Na escolha do especialista, coloquei o "(0)" apenas para continuar e não contabilizar, assim podendo colocar -1
# no CPF sem afetar o resultado!

while True:
    medOpcoes = int(input('(1) Clínico Geral  -> R$ 250,00\n(2) Nutricionista  -> R$ 150,00\n(3) Fonoaudiólogo  -> R$ 200,00\n(4) Fisioterapeuta -> R$ 150,00\n(5) Odontólogo     -> R$ 200,00\n(0) Continuar\nDigite a opção: '))
    if medOpcoes == 1:
        valorConsulta = 250
        listaEspec.append(1)
        listaDinheiro.append(valorConsulta)

    elif medOpcoes == 2:
        valorConsulta = 150
        listaEspec.append(2)
        listaDinheiro.append(valorConsulta)

    elif medOpcoes == 3:
        valorConsulta = 200
        listaEspec.append(3)
        listaDinheiro.append(valorConsulta)

    elif medOpcoes == 4:
        valorConsulta = 150
        listaEspec.append(4)
        listaDinheiro.append(valorConsulta)

    elif medOpcoes == 5:
        valorConsulta = 200
        listaEspec.append(5)
        listaDinheiro.append(valorConsulta)

    print('-=' * 12)

    # Input's e Dados
    cpf = int(input('Digite o número do CPF: '))
    if cpf == -1:
        break

    nome = str(input('Digite o seu nome: '))
    idade = int(input('Digite a sua idade: '))
    conv = str(input('Possúi convênio(S/N) ? ').upper().strip())
    if conv == 'S':
        valorConsultaFinal = valorConsulta - (valorConsulta * 0.75)
        listaDinheiro.remove(valorConsulta)
        listaDinheiro.append(valorConsultaFinal)
        listaTotalDescConv.append(valorConsultaFinal)

    consulta = int(input('(1) Primeira consulta ou (2) Retorno? '))
    if consulta == 1:
        listaPC.append(1)

    elif consulta == 2:
        listaDinheiro.pop()
        listaNomeR.append(nome)
        if conv == 'S':
            listaTotalDescConv.pop()

    # Verificações para a letra F
    if medOpcoes == 1:
        if conv == 'S' and consulta == 1:
            listaClinico.append(62.5)
        if conv == 'N' and consulta == 1:
            listaClinico.append(250)
    elif medOpcoes == 2:
        if conv == 'S' and consulta == 1:
            listaNutri.append(37.5)
        if conv == 'N' and consulta == 1:
            listaNutri.append(150)
    elif medOpcoes == 3:
        if conv == 'S' and consulta == 1:
            listaFono.append(50)
        if conv == 'N' and consulta == 1:
            listaFono.append(200)
    elif medOpcoes == 4:
        if conv == 'S' and consulta == 1:
            listaFisio.append(37.5)
        if conv == 'N' and consulta == 1:
            listaFisio.append(150)
    elif medOpcoes == 5:
        if conv == 'S' and consulta == 1:
            listaOdonto.append(50)
        if conv == 'N' and consulta == 1:
            listaOdonto.append(200)

# Questões
print('-=' * 12)
print(f'a) A quantidade de atendimentos de primeira consulta: {len(listaPC)}')
print(f'b) O valor total arrecadado pela clínica com o especialista em odontologia: R$ {sum(listaOdonto)}')
print(f'c) A relação de pacientes que não pagaram consulta por ser uma consulta de retorno:')
for nomes in listaNomeR:
    print(f'{nomes}')
print(f'd) O valor total de descontos por convênio: R$ {sum(listaTotalDescConv)}')
somaTotalP = len(listaPC) + len(listaNomeR)
print(f'e) O percentual de consultas de retorno: {((len(listaNomeR) / somaTotalP) * 100):.2f}%')
print(f'f) O valor total arrecadado pela clínica por especialista:\nClínico Geral: R$ {sum(listaClinico)}\nNutricionista: R$ {sum(listaNutri)}\nFonoaudiólogo: R$ {sum(listaFono)}\nFisioterapeuta: R$ {sum(listaFisio)}\nOdontólogo: R$ {sum(listaOdonto)}')
