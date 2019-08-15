# Projeto: mapIt.py com o módulo webbrowser
import webbrowser
webbrowser.open("www.google.com.br")  ## abrindo o navegador

# Fazendo download de arquivos da Web com o módulo requests
import requests

# Fazendo download de uma página web com a função requests.get()
response = requests.get("https://automatetheboringstuff.com/files/rj.txt")
type(response)

print(response.text[:250])

# Salvando arquivos baixados no disco rígido