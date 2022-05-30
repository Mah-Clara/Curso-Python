# Desafio 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))

print('O comprimento da hipotenusa do triângulo retângulo é de {:.2f}.'.format(co+ca))
