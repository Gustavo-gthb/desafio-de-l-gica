#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).

temperatura_farenheit = int(input('temperatura em graus Farenheit: '))
conversao_em_celsius = 5 * (temperatura_farenheit - 32) / 9
print('o valor em celsius é: ', conversao_em_celsius)