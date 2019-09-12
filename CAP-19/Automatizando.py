# CORRESPONDÊNCIA DE PADRÕES COM EXPRESSÕES REGULARES

#import re
#
# numCelular = re.compile(r"(\d\d\d-\d)-(\d\d\d\d)-(\d\d\d\d)")
# num = numCelular.search("084-9-9191-2186")
# print(num.group(1))
# print(num.group(2))
# print(num.group(3))
#
# nomes = re.compile(r"Samuel|Lima|de|Farias")
# nome = nomes.search("Lima de Farias")
# print(nome.group())

# LENDO E ESCREVENDO EM ARQUIVOS
# Processo de leitura/escrita
# ORGANIZANDO ARQUIVOS
""" Módulo shutil
O módulo shutil (shell utilities, ou utilitários de shell) contém funções que
permitem copiar, mover, renomear e apagar arquivos em seus programas
Python. Para usar as funções de shutil, inicialmente você deverá usar import shutil. """

#1- criando o arquivo
# arquivoTXT = open('gatos.txt','w')
# arquivoTXT.writelines('gato - 01')
# arquivoTXT.writelines('gato - 02')
# arquivoTXT.writelines('gato - 03')
#
# arquivoTXT.close()

# abrindoArquivoTXT = open('gatos.txt','r')
# listaGatos = abrindoArquivoTXT.readlines()
# print(listaGatos)
# arquivoTXT.close()
# arquivoTXT = open('gatos.txt','w')
# arquivoTXT.writelines('gatinhos 01')
# arquivoTXT.writelines('gatinhos 02')
# arquivoTXT.writelines('gatinhos 03')
# arquivoTXT.writelines('gatinhos 04')
# arquivoTXT.close()
#
# abrindoArquivoTXT2 = open('gatos.txt','r')
# listaGatos = abrindoArquivoTXT.readlines()
# print(listaGatos)
# abrindoArquivoTXT2.close()

# dog = open('dogs.txt','w')
# dog.write('ralf-01')
# dog.write('ralf-02')
# dog.write('ralf-03')
# dog.write('ralf-04')
# dog.close()

# leituraDogs = open('dogs.txt','r')
# listaDogs = leituraDogs.read()
# print(listaDogs)
# leituraDogs.close()

# animais = open('animais.txt','a')
# animais.write("cachorro \n")
# animais.write("gato \n")
# animais.write("periquito \n")
# animais.write("gavião \n")
# animais.write("jacaré \n")
# animais.close()

# animal = open('animais.txt','r')
# listaAnimais = animal.readlines()
# print(listaAnimais)

# Compactando arquivos com o módulo zipfile
# Lendo arquivos ZIP
import zipfile,os
caminho = os.walk('C:\\DESENVOLVIMENTO-BACK-END\\IntensivoPython\\CAP-19')

for pasta in caminho:
    print(pasta)

caminhos02 = os.chdir('C:\\DESENVOLVIMENTO-BACK-END\\IntensivoPython\\CAP-19')
arquivoZIP =zipfile.ZipFile('teste.zip')
listaDeArquivos = arquivoZIP.namelist()
print(listaDeArquivos)

# Extraindo itens de arquivos ZIP

# arquivoZIP.extractall()
# arquivoZIP.close()

# Criando arquivos ZIP e adicionando itens
# newZip = zipfile.ZipFile('newZipe.zip','w')
# newZip.write('spam.txt',compress_type=zipfile.ZIP_DEFLATED)
# newZip.close()


