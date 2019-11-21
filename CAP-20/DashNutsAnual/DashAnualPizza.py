from ReceberArquivo import ReceberArquivoCSV
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np

import DashNuts2015.DashNuts2015 as ds2015
import DashNuts2016.DashNuts2016 as ds2016
import DashNuts2017.DashNuts2017 as ds2017
import DashNuts2018.DashNuts2018 as ds2018

dadosDoAno = ReceberArquivoCSV("atividade2015.csv")


fig = plt.figure(constrained_layout=True)
gs = GridSpec(2, 2, figure=fig)

valoresCategorias2015 = [ds2015.somaBancas(), ds2015.somaSigs(), ds2015.somaSessoesClinicas(), ds2015.somaVCEbserh(), ds2015.somaVideoAulas()]
valoresCategorias2016 = [ds2016.somaBancas(), ds2016.somaSigs(), ds2016.somaSessoesClinicas(), ds2016.somaVCEbserh(), ds2016.somaVideoAulas()]
valoresCategorias2017 = [ds2017.somaBancas(), ds2017.somaSigs(), ds2017.somaSessoesClinicas(), ds2017.somaVCEbserh(), ds2017.somaVideoAulas()]
valoresCategorias2018 = [ds2018.somaBancas(), ds2018.somaSigs(), ds2018.somaSessoesClinicas(), ds2018.somaVCEbserh(), ds2018.somaVideoAulas()]
categorias = ["Bancas", "SIG's", "Sessões Clínicas", "EBSERH", "Videoaulas"]

#
explode = (0.1,0,0,0,0.1)

ax1 = fig.add_subplot(gs[0, 0])
ax1.set_title("Atividades 2015: " + str(ds2015.somaMeses()))
ax1.pie(valoresCategorias2015, explode = explode,labels = categorias, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.legend()

ax2 = fig.add_subplot(gs[1, 0])
ax2.set_title("Atividades 2016: " + str(ds2016.somaMeses()))
ax2.pie(valoresCategorias2016, explode = explode,labels = categorias, autopct='%1.1f%%', shadow=True, startangle=90)
ax2.legend()


ax3 = fig.add_subplot(gs[0, 1])
ax3.set_title("Atividades 2017: " + str(ds2017.somaMeses()))
ax3.pie(valoresCategorias2017, explode = explode,labels = categorias, autopct='%1.1f%%', shadow=True, startangle=90)
ax3.legend()

ax4 = fig.add_subplot(gs[1, 1])
ax4.set_title("Atividades 2018: " + str(ds2018.somaMeses()))
ax4.pie(valoresCategorias2018, explode = explode,labels = categorias, autopct='%1.1f%%', shadow=True, startangle=90)
ax4.legend()
#
#
fig.suptitle("PAINEL DE ATIVIDADES DO NUTS 2015 - 2018", color = "black")
plt.show()