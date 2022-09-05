"""
Tendo como dados de entrada a altura de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58
"""
while True:
    try:
        altura = input('Digite sua altura: ')

        if altura.isnumeric():
            print('Esqueceu o ponto, meu consagrado')
        else:
            peso_ideal = (72.7 * float(altura)) - 58
            print(f'Seu peso ideal é {peso_ideal:,.2f}')
            break

    except ValueError:
        print('Altura invalida')
