# PARTE 2 - VISUALIZAÇÃO DE DADOS
# CAPITULO 15 - GERANDO DADOS

#Instalando o matplotlib

import matplotlib.pyplot as plt
from math import pow
# import json

x = range(1,100)
y = []
for numeros in x:
    y.append(pow(numeros,2))

# print(y)
# matplotlib.pyplot.bar(y, height=0.9,width=0.8,bottom=None,align='center',data=None,)

# plt.plot(x,y)
# plt.show()

#Alterando o tipo do rótulo e a espessura do gráfico
# plt.plot(x, y, linewidth=5)
# plt.title("Sequência de números", fontsize = 24) #titulo do grafico
# plt.xlabel("Valor x", fontsize = 14) #nomeando os eixos
# plt.ylabel("Valor y", fontsize = 14) #nomeando os eixos
# plt.tick_params(axis='both',labelsize = 14) #Define o tamanho dos rótulos das marcações
# plt.show()

#Corrigindo o gráfico
# Plotando e estilizando pontos individuais com scatter()

# DadosEmArquivos = open('dados','w')
# json.dump(y,DadosEmArquivos)
# DadosEmArquivos.close()

# Plotando e estilizando pontos individuais com scatter()

# plt.scatter(x,y,s=2) # esse 3º argumento serve para dar uma espessura aos pontos do gráfico
# plt.title('Quadrado dos números de 1 a 100', fontsize = 14) #titulo do grafico
# plt.xlabel("Valor x", fontsize = 10) #nomeando os eixos
# plt.ylabel("Valor y", fontsize = 10) #nomeando os eixos
# plt.tick_params(axis='both',labelsize = 14) #Define o tamanho dos rótulos das marcações
# plt.show()

# Removendo os contornos dos pontos de dados
## edgecolors= 'r' ou 'red' | 'green','yellow' ou cor em inglês

# plt.scatter(x,y,edgecolors= 'r',s=2) # esse 3º argumento serve para dar uma espessura aos pontos do gráfico
# plt.title('Quadrado dos números de 1 a 100', fontsize = 14) #titulo do grafico
# plt.xlabel("Valor x", fontsize = 10) #nomeando os eixos
# plt.ylabel("Valor y", fontsize = 10) #nomeando os eixos
# plt.tick_params(axis='both',labelsize = 14) #Define o tamanho dos rótulos das marcações
# plt.show()

############ Definindo cores personalizadas #######
# c = 'red' ou RGB (1,2,4)

# plt.scatter(x,y,c='red', edgecolors= 'none',s=2) # esse 3º argumento serve para dar uma espessura aos pontos do gráfico
# plt.title('Quadrado dos números de 1 a 100', fontsize = 14) #titulo do grafico
# plt.xlabel("Valor x", fontsize = 10) #nomeando os eixos
# plt.ylabel("Valor y", fontsize = 10) #nomeando os eixos
# plt.tick_params(axis='both',labelsize = 14) #Define o tamanho dos rótulos das marcações
# plt.show()

# Usando um colormap
#cmap -> os menores valores de y tem a cor azul-claro e para os maiores valores d y azul-escuro
plt.scatter(x,y,c=y, cmap=plt.cm.Blues, edgecolors= 'none',s=2)
plt.title('Quadrado dos números de 1 a 100', fontsize = 14) #titulo do grafico
plt.xlabel("Valor x", fontsize = 10) #nomeando os eixos
plt.ylabel("Valor y", fontsize = 10) #nomeando os eixos
plt.tick_params(axis='both',labelsize = 14) #Define o tamanho dos rótulos das marcações

# Salvando seus gráficos automaticamente
plt.savefig('novoGrafico.png',bbox_inches='tight') #1º para salvar o grafico, 2º bbox_inches='tight' para remover espaço em branco
plt.show()






