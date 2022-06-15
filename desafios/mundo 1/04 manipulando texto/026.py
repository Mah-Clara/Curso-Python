# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

f = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(f.count('A')))
print('A primeita letra A apareceu na posição {}'.format(f.find('A')+1))
print('A primeita letra A apareceu na posição {}'.format(f.rfind('A')-1))