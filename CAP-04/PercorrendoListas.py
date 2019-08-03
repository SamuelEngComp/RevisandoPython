# Percorrendo uma lista inteira com um laço

nomes = ['samuel','ruanna','alzenir','joao', 'jose', 'maria']

# percorrendo cada item da lista
for nome in nomes:
     print(nome.title()) #imprimindo cada nome


     #print("Ainda estou dentro do laço FOR")


print("Como não utiliza {} no laço for... ele so executa quem esta identado dentro dele")

#OBS.: DEVEMOS PRESTAR MUITA ATENÇÃO NA IDENTAÇÃO DO CÓDIGO, POIS O PYTHON É CRUEL COM ISSO
#OBS.: Os dois-pontos no final de uma instrução for diz a Python para interpretar a próxima linha como o início de um laço.


######################################################################################################################################################
#CRIANDO LISTAS NUMERICAS
#Usando a função range()

for valor in range(1,9): #a função range() vai gerar numeros de 1 ate 8
    print(valor)

#converter o range(1,9) em uma lista
numeros = list(range(1,9))
print(numeros) #[1, 2, 3, 4, 5, 6, 7, 8]

#a função range() pode ignorar alguns numeros no intervalo pre-determidado, por exemplo:
numerosPares = list(range(0,51,2)) # range(inicio, fim, passo)
print(numerosPares) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]

#raiz quadrada dos 10 primeiros numeros
numerosParaQuadrado = range(1,11)
quadrados = []
for valor in numerosParaQuadrado:
    quadrados.append(valor**2)

print(quadrados)

#Estatísticas simples com uma lista de números
print(max(quadrados))
print(min(quadrados))
print(sum(quadrados))
soma = sum(quadrados)
qtd = len(quadrados)
media = soma/qtd
print(media)


#List comprehensions
#cria uma lista de quadrados com uma linha de codigo
quadrados2 = [valor2**2 for valor2 in range(1,11)]
print(quadrados2)

#contando ate 20
vintes = [numeros_ate_vinte for numeros_ate_vinte in range(1,21)]
print(vintes)

#contando ate 1000000
# for milhao in range(1,1000000):
#     print(milhao)
#
# milhoes = [milhao2 for milhao2 in range(1,1000001)]
# print(milhoes)

#imprimindo numeros impares
numerosImpares = []
for num in range(1,20,2):
    numerosImpares.append(num)

print(numerosImpares)

#OU

numerosImpares2 = [numeroImpar for numeroImpar in range(1,20,2)]
print(numerosImpares2)

###########################################################################
#NUMEROS MULTIPLOS DE 3
multiploDeTres = []
for multiplo in range(0,33,3):
    multiploDeTres.append(multiplo)

print(multiploDeTres)

#raiz cubica
raizCubica = [cubo**3 for cubo in range(1,11)]
print(raizCubica)

#ou
raizCubica02 = []
for cubo2 in range(1,11):
    raizCubica02.append(cubo2**3)

print(raizCubica02)

###########################################################################3333

#Trabalhando com parte de uma lista
#Fatiando uma lista
#nomes = ['samuel','ruanna','alzenir','joao', 'jose', 'maria']
nomes.append('Neymar')
print(nomes[0:4])
print(nomes[:3])
nomes.append('Messi')
nomes.append('CR7')
print(nomes[4:])
print(nomes[-2:])

#Percorrendo uma fatia com um laço
for nomePessoa in nomes[0:3]:
    print(nomePessoa)


#Copiando uma lista
nomesCopiados = nomes[:]
print(nomesCopiados)

#SE FOSSE ASSIM: nomesCopiados = nomes..... ambas estão apontando pra mesma lista, se eu adicionar um nome em uma lista,
# sera adicionado na outra lista automaticamennte


####################################################################################################################################

#TUPLAS
#DEFININDO UMA TUPLA
# OBS.: Python refere-se a valores que não podem mudar como imutáveis, e uma lista imutável é chamada de tupla.
dimensoes = (200, 50)
print(dimensoes[0])
print(dimensoes[1])

for dimensao in dimensoes:
    print(dimensao)

#SOBRESCREVENDO UMA TUPLA
for dimensao in dimensoes:
    print("Original " + str(dimensao))

dimensoes = (100, 150)
for dimensao in dimensoes:
    print("sobrescrevendo " + str(dimensao))

#TENTANDO SOBRESCREVER UMA TUPLA MAIOR
buffet = ('file','ovos','pizza')
for comidas in buffet:
    print(comidas)

buffet = ('file','ovos','pizza','macarrao')
for comidas in buffet:
    print("comidas alteradas " + comidas)

buffet = ('fileComFritas')
print(buffet)











