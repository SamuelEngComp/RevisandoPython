# trabalhando com API
# Requisitando dados usando uma chamada de API
# Instalando o pacote requests

import requests
import json

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status code: ",r.status_code)

response = r.json()
print(response.keys())

# Trabalhando com o dicionário de resposta
# print("Total de repositórios: ", response['total_count'])
# informacoesRepositorios = response['items']
#
# print("Repositórios retornados: ", len(informacoesRepositorios))
#
# primeiroRepositorio = informacoesRepositorios[0]
# print("Chave: ", len(primeiroRepositorio))
#
# for chave in sorted(primeiroRepositorio.keys()):
#     print(chave)

############ buscando meu repositorio no github
url02 = "https://api.github.com/search/users?q=user:SamuelEngComp"
s = requests.get(url02)
print("Status code: ",s.status_code)

response02 = s.json()
print(response02.keys())
print(response02.values())

print("Itens: ", response02['total_count'])