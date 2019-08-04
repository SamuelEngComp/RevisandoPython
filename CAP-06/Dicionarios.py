# Um dicionário simples
pessoa = {
    'nome' : 'samuel',
    'idade' : 26,
    'sexo' : 'masculino'
}

print(pessoa['nome'])

# ACESSANDO OS ATRIBUTOS DO DICIONARIO PESSOA

nomePessoa = pessoa['nome']
print("Meu nome é: " + pessoa['nome'].title())
#ou
print("Meu nome é: " + nomePessoa.title())

# Adicionando novos pares chave-valor
pessoa['altura'] = 1.70
pessoa['profissao'] = 'Tecnico em Informatica'

print(pessoa)

#Teste para adicionar Endereço
endereco = {
    'rua':'boa vista',
    'bairro':'boa vista',
    'numero':313,
    'cidade':'joao camara',
    'estado':'RN'
}

pessoa['endereco'] = endereco

print(pessoa) #{'nome': 'samuel', 'idade': 26, 'sexo': 'masculino', 'altura': 1.7, 'profissao': 'Tecnico em Informatica', 'endereco': {'rua': 'boa vista', 'bairro': 'boa vista', 'numero': 313, 'cidade': 'joao camara', 'estado': 'RN'}}


###########################  Começando com um dicionário vazio ################################3
print("############################################################################################################")

dicionarioVazio = {}

# Modificando valores em um dicionário

dicionarioVazio['cor'] = 'azul'
print(dicionarioVazio)

dicionarioVazio['refeicao'] = 'feijao'
print(dicionarioVazio)
dicionarioVazio['refeicao'] = 'Arroz'
print(dicionarioVazio)

# Removendo pares chave-valor
del dicionarioVazio['refeicao']
print(dicionarioVazio)

linguagensFavoritas = {
    'samuel':'java',
    'Neymar':'python',
    'Messi':'C/C++',
    'CR7':'java'
}

if 'java' in linguagensFavoritas.values():
    print("Nesta lista tem a linguagem java")
else:
    print("deu algum erro")

# Percorrendo um dicionário com um laço
# Percorrendo todos os pares chave-valor com um laço

for chave, valor in linguagensFavoritas.items():
    print("chave : " + chave)
    print("valor : " + valor)


# Percorrendo todas as chaves de um dicionário com um laço
for nome in linguagensFavoritas.keys():
    print(nome)

for nome in linguagensFavoritas:
    print(nome)
# AMBOS PRODUZEM A MESMA SAIDA

############################################################################################################
print("############################################################################################################")
for nome in sorted(linguagensFavoritas):
    print(nome)

# Percorrendo todos os valores de um dicionário com um laço
for valor in linguagensFavoritas.values():
    print(valor)
############################################################################################################
print("############################################################################################################")
for linguagem in set(linguagensFavoritas.values()): #a função SET remove os valores duplicados
    print(linguagem)



########################LISTA DE DICIONARIOS ############################################################
pessoa01 = {'nome':'samuel01','idade':26}
pessoa02 = {'nome':'samuel02','idade':27}
pessoa03 = {'nome':'samuel03','idade':28}

pessoas = [pessoa01,pessoa02,pessoa03]

for p in pessoas:
    print(p)
    print(p.keys())
    print(p.values())
    print("#################################################")



gentes = []
for g in range(20):
    gente = {'nome':'qualquerNome','idade':28}
    gentes.append(gente)

for testando in gentes[:20]:
    print(testando)

print(len(gentes))

#############Uma lista em um dicionário#############

esporte = {
    'pessoa':['jose','joao','maria'],
    'profissão':['tecnico','enfermeiro','biologo'],
    'idade':32
}
for p in esporte.values():
    print(p)

print(esporte['pessoa'])

#################### Um dicionário em um dicionário ##########################3
print(endereco)
print(pessoa) ## endereco esta dentro de pessoa





