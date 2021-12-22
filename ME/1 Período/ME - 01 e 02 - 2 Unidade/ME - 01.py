listaNome = []
listaIdade = []
listaPago = []
listaQtdDesc = []
listaNome60 = []
listaDesc = []

while True:

    #Input's necessários
    nome = str(input('Digite o seu nome: '))
    if nome == '-1':
        break
    listaNome.append(nome)
    idade = int(input('Digite sua idade: '))
    listaIdade.append(idade)
    print('-=' * 12)

    #Verificações e append's
    if idade < 5:
        ingressoDesc = 20 - (20 * 0.10)
        listaPago.append(ingressoDesc)
        listaQtdDesc.append(1)
        descIng = 20 * 0.10
        listaDesc.append(descIng)
    elif (idade >= 6) and (idade <= 12):
        ingressoDesc = 20 - (20 * 0.08)
        listaPago.append(ingressoDesc)
        listaQtdDesc.append(2)
        descIng = 20 * 0.08
        listaDesc.append(descIng)
    elif (idade >= 13) and (idade <= 25):
        ingressoDesc = 20 - (20 * 0.05)
        listaPago.append(ingressoDesc)
        listaQtdDesc.append(3)
        descIng = 20 * 0.05
        listaDesc.append(descIng)
    elif (idade >= 26) and (idade <= 60):
        listaPago.append(20.0)
    elif idade > 60:
        ingressoDesc = 20 - (20 * 0.15)
        listaPago.append(ingressoDesc)
        listaQtdDesc.append(4)
        listaNome60.append(nome)
        descIng = 20 * 0.15
        listaDesc.append(descIng)

print('-=' * 28)
print('Questões: ')

print('a) Relação dos clientes, idade e o valor do ingresso pago: ')
for i in range(len(listaIdade)):
    print(f'Nome: {listaNome[i]:9}    | Idade: {listaIdade[i]:9}    | Pago: R$ {listaPago[i]}')
print(f'b) Quantidade de pessoas com desconto: {len(listaQtdDesc)}')
print(f'c) Percentual de pessoas com desconto de 10%: {(listaQtdDesc.count(1)/len(listaPago)) * 100}%')
print(f'd) Relação dos clientes que possuem acima de 60 anos:')
for i in range(len(listaNome60)):
    print(f'{listaNome60[i]}')
print(f'e) A média do valor de descontos aplicados: R$ {sum(listaDesc) / len(listaDesc):.2f}')