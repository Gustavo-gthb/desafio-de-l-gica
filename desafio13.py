# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: Para homens: (72.7h) - 58 Para mulheres: (62.1h) - 44.7

altura = float(input('Digite a sua altura: '))
sexo = str.lower(input('qual é o seu sexo? (m/f)'))
if sexo == 'm':
    masculino = (72.7 * altura) - 58
    print(masculino)
elif sexo == 'f':
    feminino = (62.1 * altura) - 44.7
    print(feminino)
else:
    print('sexo inválido')
    