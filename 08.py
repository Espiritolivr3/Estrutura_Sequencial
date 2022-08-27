"""
Faça um Programa que pergunte quanto você ganha por hora
e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""
while True:
    try:
        hora_ganha = input("Valor da hora trabalhada: ")
        horas_trabalhadas = input('Horas trabalhadas: ')
        salario_do_mes = int(hora_ganha) * int(horas_trabalhadas)
        print(salario_do_mes)
        break

    except ValueError:
        print('Valor invalido, digite um numero')
