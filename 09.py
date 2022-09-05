"""
Faça um Programa que peça a temperatura em graus Fahrenheit,
transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""
while True:
    try:
        fahrenheit = input('Digite a tempatura em graus Fahrenheit: ')
        celsius = (int(fahrenheit) - 32) * 5 / 9
        print(celsius)
        break

    except ValueError:
        print('Digite um numero valido')
