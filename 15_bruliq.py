#bruliq.py

"""

15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: 
    salário bruto. 
    quanto pagou ao INSS. 
    quanto pagou ao sindicato. 
    o salário líquido. 
    calcule os descontos e o salário líquido, conforme a tabela abaixo: 
        + Salário Bruto : R$
        - IR (11%) : R$
        - INSS (8%) : R$
        - Sindicato ( 5%) : R$
        = Salário Liquido : R$

"""
#ganho por hora.
gph = input(
    'Digite quando você ganha por hora: '
)
#horas trabalhadas no mês.
htm = input(
    'Digite o número de horas trabalhadas no mês: '
)
#Salário bruto = ganho por hora * horas trabalhadas no mês.
sb = float(gph) * float(htm)

#Imposto de renda = 11% do salário bruto.
ir = (float(sb) * 11) /100

#INSS = 8% do salário bruto.
inss = (float(sb) * 8) / 100

# 5% do salário bruto = contribuição sindical
sind = (float(sb) * 5) / 100

#Salário Líquido = salário bruto - (imposto de renda + INSS + sindicato)
sl = sb - (float(ir) + float(inss) + float(sind))


#'\n' para dar uma linha para a tabela, espaços nas strings para alinhar
#round(xxx, 2) para restringir a casa à direita até duas.
print(
    '\n',
    '+ Salário Bruto :   R$ ',
    round(sb, 2),
    '\n',
    '- IR (11%) :        R$  ',
    round(ir, 2),
    '\n',
    '- INSS (8%) :       R$  ',
    round(inss, 2),
    '\n',
    '- Sindicato (5%) :  R$  ',
    round(sind, 2),
    '\n',
    '= Salário Liquido : R$ ',
    round(sl, 2),
    '\n'
)