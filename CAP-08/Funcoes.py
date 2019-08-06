#####  Definindo uma função ######

# def saudacao(mensagem):
#     print(mensagem)
#
# saudacao("Testando mensagem")

#####  Passando informações para uma função ######

# def saudacao(mensagem,usuario):
#     print(mensagem.title()+"\t"+usuario.title())
#
# saudacao("bem vindo","samuel")

####### Argumentos e parâmetros ######
######### Argumentos posicionais ############
######  A ordem é importante em argumentos posicionais  ########

# def saudacao(mensagem,usuario,idade):
#     dicionarioPessoa = {
#         'mensagem' : mensagem,
#         'usuario' : usuario,
#         'idade' : idade
#     }
#     return dicionarioPessoa
#
# print(saudacao("Teste de mensagem","Meu nome Samuel",26))


#########  Argumentos nomeados  #########
######### valores default - Se eu não inserir valores na chamada de uma função eles serão utilizados ########

# def saudacao(mensagem, usuario, idade, sexo = "masculino"):
#     dicionarioPessoa = {
#         'mensagem' : mensagem,
#         'usuario' : usuario,
#         'idade' : idade,
#         'sexo' : sexo
#     }
#     return dicionarioPessoa
#
# print(saudacao("Teste de mensagem","Meu nome Samuel",26)) #valor default - masculino
# print(saudacao("Teste de mensagem","Meu nome Samuel",26,"feminino")) # propriedade alterada - feminino

########################Retornando um valor #########################

# def nomeCompleto(primeiroNome, ultimoNome, nomeDoMeio = ""):
#     nomeCompletado = primeiroNome +" "+nomeDoMeio+" "+ultimoNome
#     return nomeCompletado
#
# print(nomeCompleto("Samuel","Lima","Farias"))


#############  Passando uma lista para uma função  ##################

# nomesPessoas = ['samuel','lima','farias','teste']
#
# def saudarPessoas(listaPessoas):
#     for pessoa in listaPessoas:
#         print("Bem-vindo " + pessoa.title())
#
#         #### Modificando a lista ###
#         if "maria" not in listaPessoas:
#             listaPessoas.append("maria")
#
#
# saudarPessoas(nomesPessoas)
# print("###########################################")
# nomesPessoasCopia = nomesPessoas[:]
# saudarPessoas(nomesPessoasCopia)
#
# print("###########################################")
#
# ############### Passando um número arbitrário de argumentos ##########################
# print("############### Passando um número arbitrário de argumentos ##########################")
#
# def pizza(*sabores):  ##o (*) faz com que o python crie uma tupla vazia e seja preenchida com o argumentos
#     print("PIZZA :")
#     for sabor in sabores:
#         print(sabor)
#
# pizza('calabresa','cebola','queijo')
# pizza('calabresa')
# pizza('calabresa','tomate')
#
# print("############### Passando um número arbitrário de argumentos ##########################")

#############  Misturando argumentos posicionais e arbitrários  ############################

######## OBS.:    Se quiser que uma função aceite vários tipos de argumentos, o
                # parâmetro que aceita um número arbitrário de argumentos deve ser
                # colocado por último na definição da função.  Ou seja, o argumento com ( * ) deve ser colocado no final

# def pizza(tamanho,*sabores):
#     print("Pizza tamanho: " + str(tamanho))
#     for sabor in sabores:
#         print(sabor)
#
#
# pizza(2,'calabresa', 'cebola', 'queijo')
# pizza(3,'calabresa')
# pizza(4,'calabresa', 'tomate')
##################################################################################################

# def perfil(nome, sobreNome, **informacoes):  ## os asteriscos duplos ( ** ) faz com que o python crie um dicionario vazio para aceitar as informações
#     perfilUsuario = {}
#     perfilUsuario['nome'] = nome
#     perfilUsuario['sobreNome'] = sobreNome
#
#     for chave, valor in informacoes.items():
#         perfilUsuario[chave] = valor
#
#     return perfilUsuario
#
#
# perfil_usuario = perfil('samuel','farias',location = 'salvador',cargo = 'T.I')
#
# print(perfil_usuario)


############################ Armazenando suas funções em módulos ############################
############################ Importando um módulo completo  ##############################

#from .funcaoPizza import pizza  ##ASSIM SÓ IMPORTO A FUNÇÃO PIZZA DO ARQUIVO
#from .funcaoSorvete import *    ##ASSIM EU IMPORTO TODAS AS FUNÇÕES DO ARQUIVO

#from funcaoPizza import pizza

#print(pizza(23,"teste01","teste02","teste03"))
# num01 = 3
# num02 = 34
# print(f"numero 01 = {num01}")
# print(f"numero 02 = {num02}")


import funcaoPizza

print(funcaoPizza.pizza2())


#####################################################
#                          OBSERVAÇÃO
#####################################################
############################################################3
# Realmente isso é uma peculiaridade do PyCharm, você precisa informar
# para o PyChar que no diretório onde estão os teus códigos também existem módulos que podem ser importados.
#
# Para fazer isso basta clicar com o botão direito em cima da pasta onde se encontram os teus códigos
# e ir até a opção "Mark Directory as" e clique na opção "Sources Root". Isso será o suficiente para
# você conseguir realizar os imports dos módulos que você criar.
####################################################################################3

#from funcaoSorvete import sorveteSabor ---->>> IMPORTANTO SÓ A FUNÇÃO SORVETESABOR
#import funcaoSorvete                   ----->>> IMPORTANDO TODAS AS FUNÇÕES

# alem disso eu posso importar varias funções no mesmo comando, bastando separar por virgular
# from funcaoPizza import pizza,pizza2 -->> dessa forma

#POSSO RENOMAER O IMPORT -- EXEMPLO:
#import funcaoSorvete AS FS --->>> UTILIZANDO O 'AS' PARA RENOMEAR O IMPORT

# IMPORTANDO TODAS AS FUNÇÕES DE UM MODULO
# import funcaoPizza *

