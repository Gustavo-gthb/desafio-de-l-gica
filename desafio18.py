'''
    Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''

tamanho_em_MB = int(input("informe o tamanho do arquivo a ser baixado(em MB):"))
velocidade_da_internet = int(input("informe a velocidade da internet:"))

tempo_aproximado_de_download = tamanho_em_MB / velocidade_da_internet

if tempo_aproximado_de_download >= 60:
    print("O tempo aproximado para baixar o arquivo é:",tempo_aproximado_de_download, "minuto")
elif tempo_aproximado_de_download > 60:
    print("O tempo aproximado para baixar o arquivo é:",tempo_aproximado_de_download, "minutos")
elif tempo_aproximado_de_download == 1:
    print("O tempo aproximado para baixar o arquivo é:",tempo_aproximado_de_download, "segundo")
else: 
    print("O tempo aproximado para baixar o arquivo é:",tempo_aproximado_de_download, "segundos")