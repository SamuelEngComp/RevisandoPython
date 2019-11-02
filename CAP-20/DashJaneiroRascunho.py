import matplotlib
import matplotlib.pyplot as plt
import numpy as np

dados = open('janeiro2018.csv').readlines()

data = []
atividade = []
tipo = []
participantes = []
tema = []
tempo = []


for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(",")
        data.append(linha[0])
        atividade.append(linha[1])
        tipo.append(linha[2])
        participantes.append(linha[3])
        tema.append(linha[4])
        tempo.append(linha[5])

totalDeParticipantesJaneiro = 0
for i in range(0,len(participantes)):
    totalDeParticipantesJaneiro += int(participantes[i])


totalDeTempoEmJaneiro = 0
for i in range(0, len(tempo)):
    totalDeTempoEmJaneiro += int(tempo[i])

def conversaoTempo(tempoTotalEmMinutos):
    tempoEmHoras = tempoTotalEmMinutos/60
    return round(tempoEmHoras,2)



print("Total de participantes em Janeiro: ", totalDeParticipantesJaneiro)
print("Total de tempo em Horas em Janeiro: ", conversaoTempo(totalDeTempoEmJaneiro), "h")

eventos = ['SIG','GRAVAÇÃO','SESSÃO CLÍNICA']
valores = [12, 6, 34]
explode = (0, 0.2, 0)

tituloPie = "teste"

figura01, ax1 = plt.subplots()
ax1.pie(valores, explode=explode, labels=eventos, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')
plt.title(tituloPie)
plt.show()
