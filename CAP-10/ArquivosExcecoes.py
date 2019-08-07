## LENDO DADOS DE UM ARQUIVO

#Lendo um arquivo inteiro

# objetoRetornado = open('pi.txt')
# conteudo = objetoRetornado.read()
# print(conteudo.strip()) ##estou utilizando a função rstrip() para remover a linha em branco que sobra

##Paths de arquivo
# deve-se prestar atenção ao local onde armazena os arquivos, pois pode não ser facil de encontrar o diretório

# Em sistemas Windows, use uma barra invertida (\) no lugar da barra para a frente (/)
# no path do arquivo: with open('text_files\nome_do_arquivo.txt') as
# file_object: Você também pode dizer a Python exatamente em que local
# está o arquivo em seu computador, não importando o lugar em que o
# programa em execução no momento esteja armazenado.

##########################################################################
##  Lendo dados linha a linha ##
## Criando uma lista de linhas de um arquivo
objetoRetornado = open('pi.txt')
conteudo = objetoRetornado.readlines()
print(conteudo)
lista = []
for linha in conteudo:
     lista.append(linha)
     # print(linha.rstrip())

print(lista)


#as funções rstrip(), lstrip() e strip() podem ser bastante úteis para trabalhar com o conteúdo do arquivo


### escrevendo dados em um arquivo --- stop