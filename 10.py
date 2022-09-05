"""
Faça um Programa que peça a temperatura em graus Celsius,
transforme e mostre em graus Fahrenheit.

"""

while True:
    try:
        celsius = input('Digite a tempatura em graus Celsius: ')
        fahrenheit = (int(celsius) * 9 / 5) + 32
        print(fahrenheit)
        break

    except ValueError:
        print('Digite um numero valido')
