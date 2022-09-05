"""
Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""
while True:
    try:
        print('Qual o seu sexo?')
        print('1 - Masculino')
        print('2 - Feminino')
        opcao = input('opcao: ')

        altura = float(input('Qual sua altura? '))
        masculino = 1
        feminino = 2
        peso_idealM = (72.7 * altura) - 58
        peso_idealF = (62.1 * altura) - 44.7

        if opcao == '1':
            print(f'Seu peso ideal e {peso_idealM:,.2f}')
            break
        elif opcao == '2':
            print(f'Seu peso ideal e {peso_idealF:,.2f}')
            break

    except ValueError:
        print('Opcao invalida!')
