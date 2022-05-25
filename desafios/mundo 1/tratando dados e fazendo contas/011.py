# Desafio 011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

lg = float(input("Quantos metros de largura a parede tem? "))
at = float(input('Quantos metros de altura a parede tem? '))
a = lg * at
tt = a / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {} m².\nPara pintar essa parede, você precisará de {}L de tinta.'.format(lg, at, a, tt))
