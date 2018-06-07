#17_download.py

"""
17.Faça um programa que peça o tamanho de um arquivo para download (em Mb) e a 
velocidade de um link de Internet (em Mbps), calcule e informe o tempo 
aproximado de download do arquivo usando este link (em minutos). 

Usuáros Alvo: Eu.
Sistema Alvo: Linux.
Interface: Linha de comando linux.
Requerimentos Funcionais: Inserir o tamanho de um arquivo para download (em Mb);
                          Inserir a velocidade de um link de Internet (em Mbps);
                          informe o tempo aproximado de download (em minutos);
Teste: simples - esperar uma mensagem aparecer;
               - inserir o tamanho do arquivo == tamanho;
               - inserir a velocidade de Internet == velocidade;
               - calcular e passar para minuto: tamanho / (velocidade * 60);
               - Imprimir o resultado
               
Author: victor.tbez@gmail.com
"""

#Inserir o tamanho de um arquivo para download (em Mb)
tamanho = float(
	input(
		'Insira o tamanho de um arquivo para download (em Mb): '
))
#Inserir a velocidade de um link de Internet (em Mbps)
velocidade = float(
	input(
		'Insira a velocidade de um link de Internet (em Mbps): '
))
#calcular e passar para minutos
resultado = (tamanho / velocidade) * 60

#Imprimir resultado
print(
	'\nTempo aproximado de download: %.0f Minutos\n' %resultado)
