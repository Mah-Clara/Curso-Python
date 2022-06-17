# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por casa Km acima do limite.

vl = float(input('Qual é a velocidade atual do carro? '))
if vl > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h.')
    mt = (vl - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(mt))
print('Tenha um bom dia! Dirija com segurança.')
