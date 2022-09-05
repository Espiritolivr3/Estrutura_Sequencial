"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo
"""
while True:
    try:
        int_1 = int(input('Digite um numero inteiro: '))
        int_2 = int(input('Digite um numero inteiro: '))
        real = float(input('Digite um numero real: '))
        resultado_1 = (int_1 * 2) + (int_2 * 50 / 100)
        resultado_2 = (int_1 * 3) + real
        resultado_3 = (real ** 3)

        print(f'dobro do primeiro com metade do segundo: {resultado_1}')
        print(f'soma do triplo do primeiro com o terceiro: {resultado_2:,.2f}')
        print(f'terceiro elevado ao cubo: {resultado_3:,.2f}')
        break

    except ValueError:
        print('Numero invalido.')
