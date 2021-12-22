print('A empresa contém um total de 9999 mil carros!')
v = int(input('Digite a quantidade de veículos: '))

listaP = []
for i in range(1, v + 1, 1):
    if v <= 9999:
        listaP.append(i // 1 % 10)
        segunda = listaP.count(1) + listaP.count(2)
        terca = listaP.count(3) + listaP.count(4)
        quarta = listaP.count(5) + listaP.count(6)
        quinta = listaP.count(7) + listaP.count(8)
        sexta = listaP.count(9) + listaP.count(0)
        total = segunda + terca + quarta + quinta + sexta

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print('O dia com maior restrição é Segunda')
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print('O dia com maior restrição é Terça')
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print('O dia com maior restrição é Quarta')
elif quinta > segunda and quinta > quarta and quinta > quarta and quinta > sexta:
    print('O dia com maior restrição é Quinta')
elif sexta > segunda and sexta > quarta and sexta > quinta and sexta:
    print('O dia com maior restrição é Sexta')
else:
    print('Todos os dias tem restrições iguais!!')

print('-=-' * 22)
print(f'Quantidades de veículos com restrição de saída na SEGUNDA e TERÇA: {segunda + terca}')
print(f'O percentual de veículos com permissão de saída às sexta é {100 - ((sexta / total) * 100):.2f}%')
print('-=-' * 22)