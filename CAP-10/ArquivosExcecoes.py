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
objetoRetornado = open('pi.txt','r') ## open("arquivo","modo de leitura")
conteudo = objetoRetornado
# conteudo = objetoRetornado.read()  -- LER TODAS AS LINHAS EM UMA UNICA STRING
# conteudo = objetoRetornado.readlines() -- LER TODAS AS LINHAS EM UMA LISTA
lista = []
print("Arquivo completo")
for linha in conteudo:
     lista.append(linha.strip()) ## strip() para remover a quebra de linha tanto a esquerda quanto a direita
# objetoRetornado.close()  ## fechando o arquivo


print(lista)
objetoRetornado.close()

#as funções rstrip(), lstrip() e strip() podem ser bastante úteis para trabalhar com o conteúdo do arquivo

##criar novo arquivo e escrever nele
## 1) criando um arquivo e escrevendo nele
arquivoNovo = open('nomes.txt','w')
arquivoNovo.write("Estou escrevendo no arquivo novo: SAMUEL")
arquivoNovo.close()

## 2) abrindo um arquivo e lendo ele
arquivoNovoLeitura = open('nomes.txt','r')
arquivoLido = arquivoNovoLeitura.read()
print(arquivoLido)
arquivoNovoLeitura.close()

## 1) abrindo um arquivo e escrevendo nele
arquivoNovoLeitura02 = open('nomes.txt','r')
arquivoLido02 = arquivoNovoLeitura02.readlines()

## 2) escrevendo nele
arquivoLido02.append(" Agora eu estou adicionando uma nova linha ao meu arquivo")

## 3) Abre o arquivo no modo escrita
arquivoNovoLeitura02 = open('nomes.txt','w')

## 4) Adiciona ao arquivo o texto que foi escrito
arquivoNovoLeitura02.writelines(arquivoLido02)

## 5) fecha o arquivo
arquivoNovoLeitura02.close()

## 6) Abre o arquivo no modo de leitura
arquivoNovoLeitura02 = open('nomes.txt','r')
arquivoLido02 = arquivoNovoLeitura02.read()
print(arquivoLido02)
