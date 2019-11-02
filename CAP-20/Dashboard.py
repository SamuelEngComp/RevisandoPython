import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

# dados = open('ATIVIDADES NUTS 2018.csv').readlines()
dados = open('dezembro2018.csv').readlines()

data = []
atividade = []
tipo = []
participantes = []
tema = []
tempo = []

fig1, f1_eixos = plt.subplots(ncols=2, nrows=2, constrained_layout=True) ##varias grids dividindo a tela

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(",")
        data.append(linha[0])
        atividade.append(linha[1])
        tipo.append(linha[2])
        participantes.append(linha[3])
        tema.append(linha[4])
        tempo.append(linha[5])

# print("Imprimindo o eixo DATA")
# print(data)
#
# print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
#
# print("Imprimindo o eixo ATIVIDADE")
# print(atividade)
#
# print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
#
# print("Imprimindo o eixo TIPO")
# print(tipo)
#
# print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
#
# print("Imprimindo o eixo PARTICIPANTES")
# print(participantes)
#
# print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

eixoX = 0
eixoX += (atividade.count('SESSÃO CLÍNICA DE CIRURGIA VASCULAR') or atividade.count('SESSÃO CLINICA DE CIRURGIA VASCULAR'))


# QUANTIDADE DE SESSÃO
SIG = 0
SESSAO = 0
GRAVACAO = 0
BANCA = 0
SESSAO += tipo.count('SESSÃO')
SIG += tipo.count('SIG')
GRAVACAO += (tipo.count('GRAVAÇÃO VÍDEOAULA') or tipo.count('GRAVAÇÃO VIDEOAULA') or tipo.count('GRAVAÇÃO VÍDEO AULA'))
BANCA += (tipo.count('BANCA TCC') + tipo.count('BANCA MESTRADO') + tipo.count('BANCA DOUTORADO'))

titulo = "Atividades 2018"
quantidade = "Quantidade"

plt.title(titulo)
plt.ylabel(quantidade)

# mes = ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]
# mes = ["Jan","Fev","Mar","Abr"]
# valoresDosEventos = [SIG,SESSAO, GRAVACAO,BANCA]
# plt.bar('SIG',SIG,label ="SIG" ,width=0.54)
# plt.bar('SESSÃO'+'\n'+ 'CLÍNICA',SESSAO, label ="SESSÕES" ,width=0.54)
# plt.bar('GRAVAÇÃO'+'\n'+ 'VIDEOAULA',GRAVACAO, label ="GRAVAÇÃO" ,width=0.54)
plt.bar('BANCAS'+'\n'+' EXAMINADORAS',BANCA,  label ="BANCAS" ,width=0.54,align='center')
################ inicio do codigo da documentação do matplotlib ################

# labels = ['G1', 'G2', 'G3', 'G4', 'G5']
mes = ["Jan","Fev","Mar","Abr","Mai"]
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(mes))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Men')
rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(mes)
ax.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()
################ fim do codigo da documentação do matplotlib ################

# plt.bar(mes,SIG,label ="SIG" ,width=0.54)
# plt.bar(mes,SESSAO, label ="SESSÕES" ,width=0.54)
# plt.bar(mes,GRAVACAO, label ="GRAVAÇÃO" ,width=0.54)
# plt.bar(mes,BANCA,  label ="BANCAS" ,width=0.54)
# plt.legend()



#y = [SIG,SESSAO,GRAVACAO,BANCA]

# plt.show()
