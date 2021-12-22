listaEspec = []
lista59 = []
listaDinheiro = []
valorConsulta = 0

print('*' * 24)
print('* Clínica Saúde e Vida *')
print('*' * 24)

#Na escolha do especialista, coloquei o "(0)" apenas para continuar e não contabilizar, assim podendo colocar -1
#no CPF sem afetar o resultado!

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

        if idade > 59:
            lista59.append(nome)

    print('-=' * 12)
print('-=' * 12)
print('Questões: ')

print(f'a) Clínico Geral: {listaEspec.count(1)}\n   Nutricionista: {listaEspec.count(2)}\n   Fonoaudiólogo: {listaEspec.count(3)} ')
print(f'   Fisioterapeuta: {listaEspec.count(4)}\n   Odontólogo: {listaEspec.count(5)}')
print(f'\nb) A relação nominal dos clientes que possuem o convênio com a clínica e que possuem acima de 59 anos:')
for i in range(len(lista59)):
    print(f'- {lista59[i]}')
print(f'\nc) O percentual de clientes que realizaram procedimento com um fisioterapeuta: {(listaEspec.count(4) / len(listaEspec) * 100):.2f}%')
print(f'd) O valor total arrecadado pela clínica no final do expediente: R$ {sum(listaDinheiro)}')