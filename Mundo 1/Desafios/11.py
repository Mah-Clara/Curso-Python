lg = float(input("Quantos metros de largura a parede tem? "))
at = float(input('Quantos metros de altura a parede tem? '))
a = lg * at
tt = a / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {} m².\nPara pintar essa parede, você precisará de {}L de tinta.'.format(lg, at, a, tt))
