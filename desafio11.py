#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: o produto do dobro do primeiro com metade do segundo. a soma do triplo do primeiro com o terceiro. o terceiro elevado ao cubo.

primeiro_numero_inteiro = int(input('digite um número inteiro: '))
segundo_numero_inteiro = int(input('digite um número inteiro: '))
numero_real = float(input('digite um número real: '))

primeira_calculo = 2 * primeiro_numero_inteiro * segundo_numero_inteiro / 2
segundo_calculo = primeiro_numero_inteiro * 3 + numero_real
terceiro_calculo = numero_real ** 3
print('o resultado é', primeira_calculo, segundo_calculo, terceiro_calculo )



