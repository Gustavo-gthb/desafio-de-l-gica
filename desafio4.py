# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

primeira_nota = int(input('Digite a nota do 1° Bimestre: '))
segunda_nota = int(input('Digite a nota do 2° Bimestre: '))
terceira_nota = int(input('Digite a nota do 3° Bimestre: '))
quarta_nota = int(input('Digite a nota do 4° Bimestre: '))

soma_das_notas = primeira_nota + segunda_nota + terceira_nota + quarta_nota 

media_final = soma_das_notas / 4
print('A media final é: ' + str(media_final))
