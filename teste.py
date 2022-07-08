nome = input('Digite o nome do aluno: ')
bimestre1 = input('Digite a nota do primeiro bimestre: ')
bimestre2 = input('Digite a nota do segundo bimestre: ')
bimestre3 = input('Digite a nota do terceiro bimestre: ')
bimestre4 = input('Digite a nota do quarto bimestre: ')

bimestre1 = int(bimestre1)
bimestre2 = int(bimestre2)
bimestre3 = int(bimestre3)
bimestre4 = int(bimestre4)

somanotas = (bimestre1 + bimestre2 + bimestre3 + bimestre4)  # soma das notas
somanotas = int(somanotas)
medianual = (somanotas / 4)
medianual = int(medianual)

print(f'A media anual do aluno {nome} eh {medianual}')

if medianual >= 7:
    print('Aluno aprovado')
else:
    print('Aluno reprovado')