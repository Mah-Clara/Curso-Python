# Desafio 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

# Sem a importação:
# co = float(input('Digite o comprimento do cateto oposto: '))
# ca = float(input('Digite o comprimento do cateto adjacente: '))
# hp = (co ** 2 + ca**2) ** (1/2)
# print('O comprimento da hipotenusa do triângulo retângulo é de {:.2f}.'.format(hp))

# Com importação:
from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hp = hypot(co, ca)

print('O comprimento da hipotenusa do triângulo retângulo é de {:.2f}.'.format(hp))
