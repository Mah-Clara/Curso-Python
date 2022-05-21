sl = float(input('Qual é o valor do seu salário? '))
au = sl + (sl * 15 / 100)

print('Seu salário de {} com 15% de aumento é igual a R${:.2f}.'.format(sl, au))
