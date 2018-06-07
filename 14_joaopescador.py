#joaopescador.py
"""
14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para 
contro lar o rendimento diário de seu trabalho. Toda vez que ele traz um 
peso de peixes maior que o estabelecido pelo regulamento de pesca do estado 
de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo 
excedente. João precisa que você faça um programa que leia a variável
peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a 
quantidade de quilos além do limite e na variável multa o valor da multa 
que João deverá pagar. Imprima os dados do programa com as mensagens 
adequadas. 

"""

pp = input(
    'Digite quantos kilos de peixe você tem: '
)

if float(pp) <= 50:
    print(
        'Parabéns, você não levará multa!'
    )
if float(pp) > 50:
    ps = float(pp) - 50
    m = float(ps) * 4
    print(
        '\n\n',
        'Você tem um excesso de peixe de',
        round(ps, 2),
        'kg',
        '\n',
        'Você irá pagar por esse excesso',
        round(m, 2),
        'reais.',
        '\n\n'
    )


