# Desafio 016 - Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

# Sem importação:
# n = float(input('Digite um número: '))
# print('O número {} tem a parte inteira {:.0f}.'.format(n, n))

# Com importação:
from math import trunc

n = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}.'.format(n, trunc(n)))