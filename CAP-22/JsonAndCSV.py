# TRABALHANDO COM ARQUIVOS CSV E DADOS JSON

# Módulo CSV
# Objetos Reader
import csv

arquivoCSV = open('tabelaCSV.csv')
leitorCSV = csv.reader(arquivoCSV)
dadosCSV = list(leitorCSV)
print(dadosCSV)       ## [['Nome', 'Idade', 'Sexo'], ['Samuel', '26', 'M'], ['Ruanna', '26', 'F'], ['JosÃ©', '98', 'M'], []]
print(dadosCSV[0][1]) ## Idade
print(dadosCSV[1][1]) ## 26
print(dadosCSV[2][2]) ## F
arquivoCSV.close()
"""O primeiro indice acessa a primeira lista e o segundo indice acessa o elemento mais interno da lista"""

# Lendo dados de objetos Reader em um loop for
arquivoCSV02 = open('tabelaCSV.csv')
leitorCSV02 = csv.reader(arquivoCSV02)
for linha in leitorCSV02:
     print(linha)

arquivoCSV02.close()


arquivoCSV03 = open('tabelaCSV.csv','r')
leitorCSV03 = arquivoCSV03.read()
print(leitorCSV03)
arquivoCSV03.close()

arquivoCSV04 = open('tabelaCSV.csv','r')
leitorCSV04 = arquivoCSV04.readlines()
print(leitorCSV04)
arquivoCSV04.close()


# Objetos Writer
arquivoSaida = open('saida.csv','w',newline='')
escritaSaida = csv.writer(arquivoSaida)
escritaSaida.writerow(['feijão','arroz','macarrão','ervilha','linguiça','ovos','pão','cebola','tomate','macaxeira','cenoura','mortadela','presunto','queijo','pimenta','café','açucar'])
escritaSaida.writerow(['samuel','ruanna','roberta'])
arquivoSaida.close()

arquivoSaida02 = open('saida.csv')
escritaSaida02 = csv.reader(arquivoSaida02)
for linha02 in escritaSaida02:
     print(linha02)

arquivoSaida02.close()

# Argumentos nomeados delimiter e lineterminator
"""Suponha que você queira separar as células com um caractere de tabulação no
lugar de uma vírgula e queira que as linhas tenham espaçamento duplo. Você
pode digitar algo como o seguinte no shell interativo:"""

"""
import csv
>>> csvFile = open('example.tsv', 'w', newline='')
>>> csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')  APLICANDO OS DELIMITADORES
>>> csvWriter.writerow(['apples', 'oranges', 'grapes'])

>>> csvWriter.writerow(['eggs', 'bacon', 'ham'])

>>> csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])

"""

"""
#########################
###### JSON e APIs ######
#########################
"""
# Módulo json
# Lendo JSON com a função loads()

infomacoesPessoas = {
     "nome":"Samuel Lima",
     "idade":26,
     "sexo":"M",
     "cargo":"técnico"
}

import json

# formatoJsonDasInformacoesPessoas = json.loads(infomacoesPessoas) NÃO FOI NECESSÁRIO TILIZAR ISSO, NA VERDADE NÃO FUNCIONOU
print(infomacoesPessoas)  #{'nome': 'Samuel Lima', 'idade': 26, 'sexo': 'M', 'cargo': 'técnico'}

# Escrevendo JSON com a função dumps()
formatoJsonDasInformacoesPessoas = json.dumps(infomacoesPessoas)
print(formatoJsonDasInformacoesPessoas)  ## {"nome": "Samuel Lima", "idade": 26, "sexo": "M", "cargo": "t\u00e9cnico"}

















