#tintas.py
"""
16. Faça um programa para uma loja de tintas. O programa deverá pedir o
tamanho em metros quadrados da área a ser pintada. Considere que a cobertura
da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de
latas de tinta a serem compradas e o preço total. 

"""

tam = int(
    input(
        'Tamanho em metros quadrados: '
))


if tam % 54 != 0:
    latas = int(tam / 54) + 1
else: 
    latas = tam / 54

preco = latas * 80

print (
    '%d latas' %latas
)

print (
    'R$ %.2f' %preco
)
