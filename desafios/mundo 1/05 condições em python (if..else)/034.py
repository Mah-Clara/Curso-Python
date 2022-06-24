# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#  Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para indferiores ou iguais, o aumento é de 15%.

sl = float(input('Qual é o valor do salário do funcionário? '))
if sl <= 1250:
    au = sl + (sl * 15 / 100)
else:
    au = sl + (sl * 10 / 100)
print('O salário de R${:.2f} torna a ser R${:.2f}.'.format(sl, au))