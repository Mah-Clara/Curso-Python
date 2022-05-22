# Desafio 014 - Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

c = float(input('Informe a temperatura em °C: '))
f = c * 1.8 + 32
print('A temperatura {:.2f}°C convertida em Fahrenheit é {:.2f}°F'.format(c, f))
