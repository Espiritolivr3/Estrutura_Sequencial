""""
Faça um Programa que converta metros para centímetros.
"""
while True:

    metro = input('Digite o numero de metros: ')

    if not metro.isdigit():
        print('Valor invalido imbecil, por favor digite um numero')
    else:
        metro = int(metro)
        resultado = metro * 100
        if metro <= 1:
            print(f'{metro} metro é igual a {resultado}cm')
        else:
            print(f'{metro} metros é igual a {resultado}cm')

        break
