# Desafio 018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
an = float(input('Digite o ângulo: '))
sen = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))

print('O ângulo de {:.2f} tem:\nSeno de {:.2f}\nCosseno de {:.2f}\nTangente de {:.2f}'.format(an, sen, cos, tan))
