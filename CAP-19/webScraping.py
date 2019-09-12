# Projeto: mapIt.py com o módulo webbrowser
import webbrowser
webbrowser.open("http://www.google.com.br")  ## abrindo o navegador --- no windows funcionou apenas com a URL
webbrowser.open_new("http://www.google.com.br") ## abrindo o navegador --- no Ubuntu só funcionou quando colocou http://

# Fazendo download de arquivos da Web com o módulo requests
import requests

# Fazendo download de uma página web com a função requests.get()
response = requests.get("https://automatetheboringstuff.com/files/rj.txt")
type(response)

print(response.text[:250])

# Salvando arquivos baixados no disco rígido