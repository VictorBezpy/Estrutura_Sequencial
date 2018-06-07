#salario.py
# 8. Faça um Programa que pergunte quanto você ganha por hora e o número 
#de horas trabalhadas no mês. Calcule e mostre o total do seu salário no
#referido mês.

gph = input(
    'Digite quando você ganha por hora: '
)

htm = input(
    'Digite o número de horas trabalhadas no mês: '
)

salario = float(gph) * float(htm)

print(
    'No referido mês você ganhou: ',
    round(salario, 2),
    'reais'
)