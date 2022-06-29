# Escreva um programa para aprovar o empresário bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.

c = float(input('Valor da casa: R$'))
s = float(input('Salário do comprador: R$'))
a = int(input('Quantos anos de financiamento? '))
p = c / (a * 12)
m = s * 30 / 100
print('Para pagar uma casa de R${.:2f} em {} anos.'.format(c, a), end='')
print(' a prestação será de R${.:2f}'.format(p))
if p <= m:
    print('Empréstimo pode ser concedido!')
else:
    print('Empréstimos negado!')