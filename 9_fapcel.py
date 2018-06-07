#fapcel.py
# 8. Faça um Programa que peça a temperatura em graus Farenheit,
#transforme e mostre a temperatura em graus Celsius.

f = input(
    'Digite a temperatura em Farenheit: '
)

c = (float(f) - 32) / 1.8

print(
    'Essa temperatura em Celsius é',
    round(c, 2)
)