## FORMATO DE ARQUIVO CSV
# Fazendo parse dos cabeçalhos de arquivos CSV
import csv
import tkinter
from matplotlib import pyplot as p



# arquivoCSV = open('testePlanilhaCSV.csv','r',encoding='utf-8') #abre o arquivo em modo leitura, não esquecer do encoding
# leitura = csv.reader(arquivoCSV) # ler o arquivo csv
# linhaCabecalho = next(leitura) #assim só mostra o cabeçalho
# print(linhaCabecalho)

## imprimindo todas as linha do arquivo csv
# for linha in leitura:
#      print(linha)
# arquivoCSV.close()

## criando um arquivo csv e escrevendo nele
# arquivoCSV2 = open('tabelaCSV.csv','w',encoding='utf-8')
# escreverNoArquivo = csv.writer(arquivoCSV2)
# escreverNoArquivo.writerow(('Nome','Idade','Sexo'))
# escreverNoArquivo.writerow(('Samuel','26','M'))
# escreverNoArquivo.writerow(('Ruanna','26','F'))
# escreverNoArquivo.writerow(('José','98','M'))
# arquivoCSV2.close()


# abrindoTabelaCSV = open('tabelaCSV.csv','r',encoding='utf-8').read() # eu posso ler assim, ou usando o laço for
# print(abrindoTabelaCSV)

# Extraindo e lendo dados
abrindoTabelaCSV02 = open('tabelaCSV.csv','r',encoding='utf-8')
leitorArquivo = csv.reader(abrindoTabelaCSV02)
for indice, l in enumerate(leitorArquivo):  #a função enumerate é apenas para exibir a numeração das linhas
     print(indice,l)

abrindoTabelaCSV02.close()

# Plotando dados em um gráfico

dados = [2,3,5,2,5,7,9,4,6,3,6,9,3,2,32,55,42,1,3,23,5,3,56,6,6,66,3,2]
fig = p.figure(dpi=128,figsize=(10,6))
p.plot(dados, c = 'red')
p.title("Printando Dados aleatórios em uma Imagem",fontsize = 14)
p.xlabel("Abscissas",fontsize = 12)
p.ylabel("Ordenadas",fontsize = 12)
p.show()