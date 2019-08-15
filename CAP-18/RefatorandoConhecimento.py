valor = 4.6
print(round(valor)) # 5 - round(valor) a função arredonda o valor
print(abs(valor)) # 4.6 - abs(valor) a função exibe o valor absoluto

vetor = ['gato', 'cachorro','golfinho']
vetor.append('leão') # ['gato', 'cachorro', 'golfinho', 'leão']
print(vetor)

vetor.insert(2,'tigre') #['gato', 'cachorro', 'tigre', 'golfinho', 'leão']
print(vetor)

for i in range(5):
    print(i)

for i in range(10,18):
    print(i)

import copy
vetor2 = copy.copy(vetor)
print(vetor2)

# DICIONÁRIOS E ESTRUTURAÇÃO DE DADOS

nomeCompleto = {
    "nome":"samuel",
    "sobrenome":"farias",
    "idade":26,
    "profissão":"Técnico em Tecnologia da Informação",
    "formação":"Graduado em Engenharia de Computação"
}

for chave, valor in nomeCompleto.items():
    print(chave, " - ",valor)
    print("Existe: " + str(nomeCompleto.get('nome',0)))
    print("Não existe: " + str(nomeCompleto.get('altura', 0)))

nomeCompleto['altura'] = 1.70
print(nomeCompleto)

print("##############################################################")
for chave, valor in nomeCompleto.items():
    print(chave, " - ",valor)
    print("Existe: " + str(nomeCompleto.get('nome',0)))
    print("Não existe: " + str(nomeCompleto.get('altura', 0)))

print("##############################################################")
################# APRESENTAÇÃO ELEGANTE
# import pprint
#pprint() e pformat()

##############  MANIPULAÇÃO DE STRINGS #####################
# Tabela 6.1 – Caracteres de escape
# Caractere de escape Exibido como
# \' Aspas simples     --->>> ' bob\'s '
# \" Aspas duplas
# \t Tabulação
# \n Quebra ou mudança de linha
# \\ Barra invertida


# Strings puras
print('testando string puras bob\'s')
print("testando string puras bob's")
print(r'testando string puras bob\'s')

"""teste comentario multiplo"""
print("teste")


















