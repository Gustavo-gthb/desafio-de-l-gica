'''
    Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
    
'''

letra_digitada = input("Digite a letra a ser verificada: ")

letra_em_maiusculo = letra_digitada.upper()

if letra_em_maiusculo == "F":
    print("Feminino")
elif letra_em_maiusculo == "M":
    print("Masculino")
else:
    print("Sexo inválido")