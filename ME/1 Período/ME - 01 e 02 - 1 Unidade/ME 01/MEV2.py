from random import randint

v = int(input('Digite a quantidade de carros: '))

listaP = []
for i in range(1, v + 1, 1):
        x = randint(1, 9999)
        listaP.append(x // 1 % 10)
        segunda = listaP.count(1) + listaP.count(2)
        terca = listaP.count(3) + listaP.count(4)
        quarta = listaP.count(5) + listaP.count(6)
        quinta = listaP.count(7) + listaP.count(8)
        sexta = listaP.count(9) + listaP.count(0)
        total = segunda + terca + quarta + quinta + sexta


print('-=-' * 24)
print(f'Finais das placas dos carros selecionados: {listaP}')
print(f'a) Quantidades de veículos com restrição de saída na SEGUNDA e TERÇA: {segunda + terca}')
print(f'b) O percentual de veículos com permissão de saída às sexta é {100 - ((sexta / total) * 100):.2f}%')
if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print('c) O dia com maior restrição é Segunda')
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print('c) O dia com maior restrição é Terça')
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print('c) O dia com maior restrição é Quarta')
elif quinta > segunda and quinta > quarta and quinta > quarta and quinta > sexta:
    print('c) O dia com maior restrição é Quinta')
elif sexta > segunda and sexta > quarta and sexta > quinta and sexta:
    print('c) O dia com maior restrição é Sexta')
else:
    print('Todos os dias tem restrições iguais!!')
print('-=-' * 24)