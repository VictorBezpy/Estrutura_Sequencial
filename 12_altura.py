#altura.py
# 12. Tendo como dados de entrada a altura de uma pessoa, construa um 
#algoritmo que calcule seu peso ideal, usando a seguinte
#fórmula: (72.7*altura) - 58 

a = input(
    'Digite sua altura em metros: '
)

p = (72.7 * float(a) - 58)

print(
    'Seu peso ideal é',
    round(p, 2),
    'kg'
)