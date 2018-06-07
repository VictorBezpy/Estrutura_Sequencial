#quadrado.py
# 7. Faça um Programa que calcule a área de um quadrado, em seguida 
#mostre o dobro desta área para o usuário. 

l = input(
    'Digite a medida de um dos lados do quadrado: '
)

a = float(l) ** 2

a2 = a * 2

print(
    'A área do quadrado é ',
    round(a, 2),
    'e o dobro desta área é ',
    round(a2, 2)
)