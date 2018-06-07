#intreal.py
# 11. Faça um Programa que peça 2 números inteiros e um número real
#calcule e mostre

i1 = input(
    'Digite um número inteiro: '
)

i2 = input(
    'Digite outro número inteiro: '
)

r = input(
    'Agora digite um número real: '
)

#o produto do dobro do primeiro com metade do segundo

s1 = (int(i1) * 2) + (int(i2) / 2)

#a soma do triplo do primeiro com o terceiro

s2 = (int(i1) * 3) + float(r)

#o terceiro elevado ao cubo

s3 = float(r) ** 3

print(
    'o produto do dobro do primeiro com metade do segundo é',
    s1,
    '\n'
    'a soma do triplo do primeiro com o terceiro é',
    s2,
    '\n'
    'o terceiro elevado ao cubo é',
    round(s3, 2)
)