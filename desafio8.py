#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = int(input('Quanto você ganha por hora? '))
horas_trabalhadas = int(input('quantas horas você trabalha no mês?'))
salario_no_mes = valor_hora * horas_trabalhadas
print('o seu salário mensal é:', salario_no_mes)
