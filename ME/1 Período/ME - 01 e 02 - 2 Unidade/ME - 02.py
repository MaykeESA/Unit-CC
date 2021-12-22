listaNome = []
listaIdade = []
listaPagoFE = []
listaPago = []
listaIngressoadd = []
listaNome100 = []
listaQtd25 = []
qtdIngresso = 0
ingressoDesc = 0

print('*' * 9)
print('* Circo *')
print('*' * 9)
print('\nDigite -1 no nome do cliente para receber as estastícas!')

while True:
    #Input's necessários
    nome = str(input('\nDigite o seu nome (Cliente): '))
    if nome == '-1':
        break
    listaNome.append(nome)

    idade = int(input('Digite sua idade (Cliente): '))
    listaIdade.append(idade)

    acompanhante = str(input('Deseja comprar mais ingressos (S/N)? ').upper().strip())
    if acompanhante == 'S':
        qtdIngresso = int(input('Quantos ingressos? '))
        listaIngressoadd.append(qtdIngresso)
        for i in range(1, qtdIngresso + 1, 1):
            print('-=' * 19)
            str(input('Digite o seu nome (Acompanhante): '))
            int(input('Digite a idade (Acompanhante): '))

    print('-=' * 19)

    #Verificações e append's
    #FE = Faixa Etária
    if idade < 5:
        ingressoDesc = 20 - (20 * 0.10)
        listaPagoFE.append(ingressoDesc)

    elif (idade >= 6) and (idade <= 12):
        ingressoDesc = 20 - (20 * 0.08)
        listaPagoFE.append(ingressoDesc)

    elif (idade >= 13) and (idade <= 25):
        ingressoDesc = 20 - (20 * 0.05)
        listaPagoFE.append(ingressoDesc)

    elif (idade >= 26) and (idade <= 60):
        listaPagoFE.append(20.0)

    elif idade > 60:
        ingressoDesc = 20 - (20 * 0.15)
        listaPagoFE.append(ingressoDesc)

    if qtdIngresso == 1:
        valorIngresso = ingressoDesc - (20 * 0.25)
        listaPago.append(valorIngresso)
        listaQtd25.append(1)

    elif qtdIngresso == 2:
        valorIngresso = ingressoDesc - (20 * 0.5)
        listaPago.append(valorIngresso)

    elif qtdIngresso == 3:
        valorIngresso = ingressoDesc - (20 * 0.75)
        listaPago.append(valorIngresso)

    elif qtdIngresso >= 4:
        listaPago.append(0.0)
        listaNome100.append(nome)


print('-=' * 28)
print('Questões: ')

print('a) A relação nominal dos clientes com 100% de desconto combo no seu ingresso:')
for i in range(len(listaNome100)):
    print(f'{listaNome100[i]}')
print(f'b) A quantidade de ingressos adicionais que foram comprados: {sum(listaIngressoadd)}')
print(f'c) O percentual de clientes que tiveram desconto combo de 25%: {((sum(listaQtd25)/len(listaNome)) * 100):.2f}%')
print(f'd) A média do valor de ingressos pagos por clientes com combo: R$ {(sum(listaPago) / len(listaNome)):.2f}')