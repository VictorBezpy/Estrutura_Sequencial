"""
3. Faça um Programa que peça dois números e imprima a soma. 
Problema: Fazer com que o computador some dois números inteiros.
Usuáros Alvo: Eu.
Sistema Alvo: Linux.
Interface: Linha de comando linux.
Requerimentos Funcionais: Mostrar uma mensagem; 
                          Inserir os dois números a serem somados;
                          mostrar o resultado da soma;
Teste: simples - esperar uma mensagem aparecer;
               - inserir primeiro número == n1;
               - inserir segundo número == n2;
               - somar n1 + n2;
               - mostrar resultado;
               
Mantenedor: victor.tbez@gmail.com
"""
# 1. Mensagem inicial;
print('Vamos somar')

# 2. Inserir primeiro número da soma;
n1 = input('digite o primeiro numero da soma: ')

# 3. Inserir segundo número da soma;
n2 = input('digite o segundo mumero da soma: ')

# 4. Somar os dois números (para que haja uma soma e não uma simples junção dos dois números é necessário 'int');
r = int(n1) + int(n2)

# 5. Mostrar o resultado (str(r) para que se concatenar string com números).
# ou print('o resultado é: %s' %r)
print('o resultado é: ', r)
