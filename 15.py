"""
Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês. Calcule e mostre o total
do seu salário no referido mês, sabendo-se que são
descontados 11% para o Imposto de Renda, 8% para o INSS e
5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido
até tal salario nao paga IR
até tal salario é 8% de inss e nao 11%
"""

while True:
    try:
        hora_ganha = input("Valor da hora trabalhada: ")
        horas_trabalhadas = input('Horas trabalhadas: ')
        salario_do_mes = float(hora_ganha) * float(horas_trabalhadas)
        descontos = (salario_do_mes * (13 / 100))
        salario_minimo_irr = 1941.00
        salario_com_2descontos = salario_do_mes - descontos

        if salario_do_mes > salario_minimo_irr:
            desconto_irr = (salario_do_mes * (24 / 100))
            salario_com_3descontos = (salario_do_mes - desconto_irr)
            print(f'Seu salario com os descontos do IRR, INSS e Sindicato fica R$ {salario_com_3descontos:,.2f}.')
            break
        else:
            print(f'Seu salario do mes com os descontos do INSS e Sindicato fica R$ {salario_com_2descontos:,.2f}')
            break

    except ValueError:
        print('Digite um valor valido!')
