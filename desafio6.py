# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

raio_do_circulo = int(input('Digite o raio de um círculo: '))
area = math.pi * raio_do_circulo ** 2
print('area do círculo é: ', area)