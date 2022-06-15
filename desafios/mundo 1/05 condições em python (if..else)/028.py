# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
cp = randint(0, 5) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jg = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jg == cp:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não {}!'.format(cp, jg))