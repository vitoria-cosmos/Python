# Programa que calcula a média dos 4 bimestres
soma = 0
for c in range(1, 5):
    n = float(input('Qual a nota do {}° bimestre? '.format(c)))
    soma = n + soma
    media = soma / c
print('A soma das nota é igual a: {} e a média do bimestre foi de: {}.'.format(soma, media))





