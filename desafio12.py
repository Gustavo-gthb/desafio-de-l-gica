# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura_da_pessoa = float(input("Digite sua altura: "))
peso_ideal = (72.7 * altura_da_pessoa) - 58
print('o seu peso ideal é:', peso_ideal)