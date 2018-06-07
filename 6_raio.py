#raio.py
# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre 
#sua área.

r = input(
    'Digite o raio do círculo: '
)

a = (float(r) ** 2) * 3.14

print(
    'A área do círculo é: ',
    round(a, 2)
)