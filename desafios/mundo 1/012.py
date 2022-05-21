# Desafio 012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

vl = float(input('Qual é o preço do produto? '))
des = vl - (vl * 5 / 100)

print('O preço do produto de {} com 5% de desconto é R${:.2f}.'.format(vl, des))
