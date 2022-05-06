# ler as planilhas e gravar os dados que faltam na planilha geral csv com base no código dado

# ler a planilha 

import csv


def ler_planilha_gravar_temp(arquivo_planilha):
  with open( arquivo_planilha, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter = ' ')
    


arquivo_planilha = input(f"Entre o nome do arquivo a ser lido => ")

ler_planilha_gravar_temp(arquivo_planilha)





