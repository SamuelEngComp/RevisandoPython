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

nomesPessoas = ['samuel','lima','farias','teste']

def saudarPessoas(listaPessoas):
    for pessoa in listaPessoas:
        print("Bem-vindo " + pessoa.title())

        #### Modificando a lista ###
        if "maria" not in listaPessoas:
            listaPessoas.append("maria")


saudarPessoas(nomesPessoas)
print("###########################################")
nomesPessoasCopia = nomesPessoas[:]
saudarPessoas(nomesPessoasCopia)

print("###########################################")















