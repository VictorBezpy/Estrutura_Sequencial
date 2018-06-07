#mporcm.py
# 5. Faça um Programa que converta metros para centímetros.

m = input(
    'Digite a medida em metros: '
)
cm = float(m) * 100
print(
    'Essa medida em centímetros é: ',
    round(cm, 2),
    'cm'
)