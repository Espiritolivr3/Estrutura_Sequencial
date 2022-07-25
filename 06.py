"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
while True:
    raio = input('Digite o raio do circulo: ')
    if raio.isdigit():
        break
area = 3.14 * (int(raio) * int(raio))

print(area)

