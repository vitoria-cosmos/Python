nome = input('Qual é o seu nome? ')
idade = int(input('Qual é a sua idade? '))
if idade >= 18:
    print('Você é maior de idade {}!'.format(nome))
else:
    print('Você é menor de idade {}!'.format(nome))

