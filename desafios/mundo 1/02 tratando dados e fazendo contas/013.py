# Desafio 013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sl = float(input('Qual é o valor do seu salário? '))
au = sl + (sl * 15 / 100)

print('Seu salário de {} com 15% de aumento é igual a R${:.2f}.'.format(sl, au))
