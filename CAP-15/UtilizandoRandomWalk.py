## Gerando vários passeios aleatórios
import matplotlib.pyplot as plt
from randomWalk import RandomWalk
rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x,rw.y,c=rw.y,cmap=plt.cm.Blues, edgecolors= 'none',s=15)
plt.title('Caminhada aleatória', fontsize = 12) #titulo do grafico
plt.xlabel("Valor x", fontsize = 9) #nomeando os eixos
plt.ylabel("Valor y", fontsize = 9) #nomeando os eixos
plt.tick_params(axis='both',labelsize = 12) #Define o tamanho dos rótulos das marcações
# plt.figure(dpi=128, figsize=(10, 6)) para a figura ajusta com a resolução da tela
plt.plot()
# plt.show()

########  Lançando dados com o Pygal
# Eles são úteis em visualizações apresentadas em telas de tamanhos diferentes, pois são
# automaticamente escaladas para se adequar à tela de quem as estiver vendo.

import pygal
graficoDeBarras = pygal.Bar()
graficoDeBarras._title = 'Uso dos Navegadores'
graficoDeBarras.x_labels = map(str,range(2000, 2019))

graficoDeBarras.add('Google',[2,4,2,2,3,1,43,58,9,13,1])
graficoDeBarras.add('IE',[92,4,2,5,3,1,4,8,3,3,1])
graficoDeBarras.add('Firefox',[92,4,13,5,3,1,3,58,39,173,1])
graficoDeBarras.add('Opera',[11,2,2,0,3,18,43,8,3,1,1])
graficoDeBarras.render_to_file('graficoDeBarras.svg')
# graficoDeBarras.render()
graficoDeBarras.render_in_browser()