'''
Faça um Programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor.
    Acrescente 10% de folga e sempre arredonde os valores para cima,
    isto é, considere latas cheias.
'''

import math

# área a ser pintada em metros quadrados
area_a_ser_pintada = int(input("Tamanho da área em metros quadrados a ser pintada:"))

# calculo de quantos litros de tint é necessesário para cubrir a área em metros quadrados
cobertura_da_tinta = area_a_ser_pintada / 6

# calculo de quantos galões ou latas seriam necessários para cobrir a área a ser pintada
litros_necessarios_galao = cobertura_da_tinta / 3.6
litros_necessarios_lata = cobertura_da_tinta / 18



# transforma um valor menor do que zero em 1
resultado1 = max(litros_necessarios_galao, 1)
resultado2 = max(litros_necessarios_lata, 1)

# arredonda um número decimal para um inteiro
arredondar_resultado1 = math.ceil(resultado1)
arredondar_resultado2 = math.ceil(resultado2)




# calculo do valor total gasto em galao e latas respectivamente
total_galao = arredondar_resultado1 * 25
total_latas = arredondar_resultado2 * 80



print("O valor em latas de 18 litros é: R$", total_latas, "reais")
print("O valor em total em galões é: R$", total_galao, "reais")

cobertura_variavel_lata = cobertura_da_tinta / 18

if cobertura_variavel_lata < 18:
    cobertura_variavel_galao = cobertura_variavel_lata / 3.6
    
cobertura_variavel_lata = math.ceil(cobertura_variavel_lata)
cobertura_variavel_galao = math.ceil(cobertura_variavel_galao)

total_variavel_lata = cobertura_variavel_lata * 80
total_variavel_galao = cobertura_variavel_galao * 25

total_da_mescla = total_variavel_galao + total_variavel_lata

print("A mescla de galões e tintas é: R$", total_da_mescla, "reais" )

   


    
