'''
    Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

letra_a_ser_comparada = str(input("Digite uma letra para verificar se ela é vogal ou consoante: "))

letra_a_ser_comparada_em_maiusculo = letra_a_ser_comparada.upper()  

vogais = ["A", "E" , "I" , "O", "U"]

if letra_a_ser_comparada_em_maiusculo not in vogais:
    print("É uma consoante:", letra_a_ser_comparada_em_maiusculo)
else:
    print("É uma vogal:", letra_a_ser_comparada_em_maiusculo)