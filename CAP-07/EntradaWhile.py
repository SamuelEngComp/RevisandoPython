# Como a função input() trabalha
# nome = input("Digite seu nome: ")
# print("Seu nome é: " + nome)

###################### Usando int() para aceitar entradas numéricas #################################3
# idade = input("Digite sua idade: ")
# idade = int(idade) #numero inteiro
# print("Sua idade é: " + str(idade))

#################### Operador de módulo ##################
# (%) operador de modulo - resto da divisao

# multiplo = input("Digite um numero: ")
# multiplo = int(multiplo)
#
# if multiplo%10 == 0:
#     print("multiplo de 10")
# else:
#     print("Não é multiplo de 10")

################################ Introdução aos laços while ############################

# numero = 1
#
# while numero <= 10:
#     print(numero)
#     numero+=1
#
# #BREAK E CONTINUE - podem ser utilizados para controlar o fluxo do while
#
# ingredientes = ["calabrresa","cebola"]
# ingrediente = ""
# while ingrediente != "sair":
#     ingrediente = input("digite o ingrediente ou sair: ")
#     ingredientes.append(ingrediente)
#
# ingredientes.remove("sair")
# print("Ingredientes: " + str(ingredientes))

#############################################################################

# flag = 0
# while flag <= 10:
#     idade = input("Digite sua idade: ")
#     idade = int(idade)
#     if idade < 3:
#         print("ingresso gratuito")
#     elif idade >= 3 and idade <= 12:
#         print("ingresso custará 10 reais")
#     elif idade > 12:
#         print("ingresso custará 15 reais")
#
#     flag += 1


#######################################  Usando um laço while com listas e dicionários #############################33
####################################### Transferindo itens de uma lista para outra #######################################

# usuariosNaoConfirmados = ['samuel','lima','farias']
# usuariosConfirmados = []
#
# while usuariosNaoConfirmados:
#     usuarioAtual = usuariosNaoConfirmados.pop()
#     print("Usuario confirmado: " + usuarioAtual)
#     usuariosConfirmados.append(usuarioAtual)
#
# print("Usuarios confirmados: " + str(usuariosConfirmados))

######################  Removendo todas as instâncias de valores específicos de uma lista  ###################
animais = ["cachorro","gato","cachorro","gato","cachorro","gato","cachorro","gaviao","cavalo","passarinho"]

while "cachorro" in animais:
    animais.remove("cachorro")

print(animais)

while "gato" in animais:
    animais.remove("gato")

print(animais)


#####################  Preenchendo um dicionário com dados de entrada do usuário  #######################
resposta = {}
ativo = True
while ativo:
    nome = input("Digite seu nome: ")
    resposta["nome"] = nome
    res = input("Verdadeiro YES, Falso NO: ")
    resposta["resposta"] = res

    if resposta["resposta"] == "YES":
        ativo = True
    elif resposta["resposta"] == "NO":
        ativo = False


for chave, valor in resposta.items():
    print(chave)
    print(valor)


























