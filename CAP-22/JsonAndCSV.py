# TRABALHANDO COM ARQUIVOS CSV E DADOS JSON

# Módulo CSV
# Objetos Reader
import csv

arquivoCSV = open('tabelaCSV.csv')
# leitorCSV = csv.reader(arquivoCSV)
# dadosCSV = list(leitorCSV)
# print(dadosCSV)       ## [['Nome', 'Idade', 'Sexo'], ['Samuel', '26', 'M'], ['Ruanna', '26', 'F'], ['JosÃ©', '98', 'M'], []]
# print(dadosCSV[0][1]) ## Idade
# print(dadosCSV[1][1]) ## 26
# print(dadosCSV[2][2]) ## F

"""O primeiro indice acessa a primeira lista e o segundo indice acessa o elemento mais interno da lista"""

# Lendo dados de objetos Reader em um loop for
leitorCSV02 = csv.reader(arquivoCSV)
for linha in leitorCSV02:
    print(linha)

# Objetos Writer