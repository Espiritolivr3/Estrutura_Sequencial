from math import ceil
"""
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados
da área a ser pintada. Considere que a cobertura da tinta
é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a
quantidades de latas de tinta a serem compradas e o preço total.
"""


def calculo():
    metros_quadrados = input('Qual o tamanho da area a ser pintada, \nem metros quadrados? ')
    area_cobertura = int(metros_quadrados) / 3
    latas_de_tinta = area_cobertura / 18
    latas_de_tinta = ceil(latas_de_tinta)
    valor_total = latas_de_tinta * 80
    return latas_de_tinta, valor_total


tinta, valor = calculo()
print(f'Voce precisa de {tinta} litros de tinta.')
print(f'Valor total: R${valor},00')
