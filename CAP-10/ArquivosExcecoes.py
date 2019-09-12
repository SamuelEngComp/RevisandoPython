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
# objetoRetornado = open('pi.txt','r') ## open("arquivo","modo de leitura")
# conteudo = objetoRetornado
# conteudo = objetoRetornado.read()  -- LER TODAS AS LINHAS EM UMA UNICA STRING
# conteudo = objetoRetornado.readlines() -- LER TODAS AS LINHAS EM UMA LISTA
# lista = []
# print("Arquivo completo")
# for linha in conteudo:
#      lista.append(linha.strip()) ## strip() para remover a quebra de linha tanto a esquerda quanto a direita
# objetoRetornado.close()  ## fechando o arquivo


# print(lista)
# objetoRetornado.close()

#as funções rstrip(), lstrip() e strip() podem ser bastante úteis para trabalhar com o conteúdo do arquivo

##criar novo arquivo e escrever nele
## 1) criando um arquivo e escrevendo nele
arquivoNovo = open('nomes.txt','w')
arquivoNovo.write("Estou escrevendo no arquivo novo: SAMUEL - 2019")
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
arquivoLido02.append(" Agora eu estou adicionando uma nova linha ao meu arquivo 2")

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


## PODEMOS ABRIR UM ARQUIVO EM MODOS DISTINTOS
## a) EM MODO DE LEITURA (' r ')
## b) EM MODO DE ESCRITA (' w ')
## c) EM MODO DE CONCATENAÇÃO (' a ')
## d) EM MODO DE LEITURA E ESCRITA(' r+ ')

# NOTA Python escreve apenas strings em um arquivo-texto. Se quiser
# armazenar dados numéricos em um arquivo-texto, será necessário
# converter os dados em um formato de string antes usando a função
# str().

# testeConcatenacao = open('testeConcatenacao.txt','a')
# testeConcatenacao.write('Eu criei esse arquivo concatenação para testar se funciona mesmo \n')
# testeConcatenacao.write("Agora eu digitei outra linha para concatenar com a linha anterior")
# testeConcatenacao.close()
#
# testeConcatenacao = open('testeConcatenacao.txt','r')
# testeConcatenacaoLeitura = testeConcatenacao.readlines()
# print(testeConcatenacaoLeitura)
# testeConcatenacao.close()

################################## AGORA VAMOS REVISAR EXCEÇÕES ##############################################
### Tratando a exceção ZeroDivisionError
### Usando blocos try-except

# try:
#      print(5/0)
# except ZeroDivisionError:
#      print("Impossivel dividir 5 por 0")

## Usando exceções para evitar falhas

# print("Digite o divisor e o dividendo")
# print("Digite 'q' para sair")
# while True:
#      num01 = input("Digite o primeiro número: ")
#      if num01 == 'q':
#           break
#
#      num02 = input("Digite o segundo número: ")
#      if num02 == 'q':
#           break
#
#      try:
#           resposta = int(num01)/int(num02)
#      except ZeroDivisionError:
#           print("Impossível realizar essa divisão")
#
#      else:
#           print("A resposta é: " + str(resposta))



### Tratando a exceção FileNotFoundError
## O IDEAL QUANDO FOR EXECUTAR A ABERTURA DE UM ARQUIVO É COLOCAR A FUNÇÃO OPEN() DENTRO DE UM TRY-EXCEPT
# ex.:

# try:
#      arquivoNovoLeitura = open('nomes.txt','r')
#      print("Arquivo encontrado")
# except FileNotFoundError:
#      print("Arquivo não encontrado - 404 - notFound")

## Analisando textos
## Usaremos o método de string split(), que cria uma lista de palavras a partir de uma string.

# titulo = 'Alice no pais das maravilhas'
# listaDePalavras = titulo.split() #Removeu os espaços entre as palavras
# print(listaDePalavras)
# listaDePalavrasDoArquivoNome = arquivoNovoLeitura.read()
# listaDePalavras.append(listaDePalavrasDoArquivoNome.split())
# print(listaDePalavras)
# print(len(listaDePalavras))
# arquivoNovoLeitura.close()

## Trabalhando com vários arquivos
# Falhando silenciosamente
### -->> o python tem uma instrução PASS que é utilizada no except para que quando ocorra um erro e quando for lançado
### -->> uma except não lance a except.

######################## Armazenando dados ##############################
# Usando json.dump() e json.load()
#A função json.dump() aceita dois argumentos: um dado para armazenar e um objeto arquivo que pode ser usado para armazenar o dado.

import json
# numeros = [2,3,5,7,11,13]
#
# arquivoNovoEscrita = open('arquivoNovo','w')
# json.dump(numeros, arquivoNovoEscrita)  # para armazenar a lista numbers no arquivo
# arquivoNovoEscrita.close()
#
# arquivoNovoEscrita = open('arquivoNovo','r')
# valoresDoArquivo = json.load(arquivoNovoEscrita) # Carregando os valores armazenado no arquivo
# print(valoresDoArquivo)

################################### Salvando e lendo dados gerados pelo usuário ######################################
## armazenar dados dos usuarios

userName = input("Digite seu nome: ")
dadosUsuario  = open('dadosDoUsuario.txt','w')
json.dump(userName, dadosUsuario)
dadosUsuario.close()

dadosUsuario  = open('dadosDoUsuario.txt','r')
dadosDoArquivoUsuario = json.load(dadosUsuario)
print(dadosDoArquivoUsuario)
dadosUsuario.close()

# Refatoração












