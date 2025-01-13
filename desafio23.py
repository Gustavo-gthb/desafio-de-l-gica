'''
    Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar: A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; A mensagem "Reprovado", se a média for menor do que sete; A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

primeira_nota_parcial = int(input("Digie a primeira nota:"))

segunda_nota_parcial = int(input("Digite a segunda nota:"))

soma_das_medias = primeira_nota_parcial + segunda_nota_parcial

media_das_notas = soma_das_medias / 2 

if media_das_notas >= 7 :
    print("Aprovado", media_das_notas)
    
if media_das_notas < 7 :
    print("Reprovado", media_das_notas)
    
if media_das_notas == 10 :
    print("Aprovado com distinção", media_das_notas)
    
    