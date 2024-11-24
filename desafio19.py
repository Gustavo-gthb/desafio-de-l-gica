'''
    Faça um Programa que peça dois números e imprima o maior deles.
'''

primeiro_numero = int(input("Digite o primeiro número:"))
segundo_numero = int(input("Digite o segundo número:"))

if primeiro_numero > segundo_numero:
    print("O número maior é o primeiro:", primeiro_numero)
elif primeiro_numero == segundo_numero:
    print("Os números são iguais, digites números diferentes!")
else:
    print("O maior número é o segundo:", segundo_numero)