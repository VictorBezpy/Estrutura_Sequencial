#alturahem.py
# 13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um 
#algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#   Para homens: (72.7*h) - 58 
#   Para mulheres: (62.1*h) - 44.7 

a = input(
    'Digite sua altura em metros: '
)

s = input(
    'Digite seu sexo (masculino ou feminino): '
)

if s == 'masculino':
    p = (float(a) * 72.7) - 58

if s == 'feminino':
    p = (float(a) * 62.1) - 44.7

print(
    'Seu peso ideal é',
    round(p, 2),
    'kg'
)