'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.

Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

'''

import math

area_a_ser_pintada = float(input('Digite a área em metros quadrados a ser pintada: '))
cobertura_da_tinta = area_a_ser_pintada / 3
latas_necessarias = math.ceil((cobertura_da_tinta / 18))
print(latas_necessarias)

if latas_necessarias <= 0:
    latas_necessarias + 1
else:
    latas_necessarias
    
print(latas_necessarias)

valor_a_ser_pago = latas_necessarias * 80

if latas_necessarias == 1:
    print ('você precisará comprar:', latas_necessarias, 'lata de tinta', 'e pagará como preço total:', valor_a_ser_pago, 'Reais' )
else:
    print ('você precisará comprar:', latas_necessarias, 'latas de tinta', 'e pagará como preço total:', valor_a_ser_pago, 'Reais')