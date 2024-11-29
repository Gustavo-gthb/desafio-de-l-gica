'''
    Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''

valor_a_ser_comparado = int(input('Digite o número a ser comparado:'))

if valor_a_ser_comparado > 0:
    print("O número digitado é positivo: ", valor_a_ser_comparado)
elif valor_a_ser_comparado < 0:
    print("O número digitado é negativo:", valor_a_ser_comparado)
else:
    print("O valor digitado é zero!")
    