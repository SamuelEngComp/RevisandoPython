import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np

from DashNuts2015.DashNuts2015 import dadosDoAno as dash2015
from DashNuts2016.DashNuts2016 import dadosDoAno as dash2016
from DashNuts2017.DashNuts2017 import dadosDoAno as dash2017
from DashNuts2018.DashNuts2018 import dadosDoAno as dash2018

participantesPorCategoria2015 = [dash2015.participantesApenasDasBancas(), dash2015.participantesApenasDoSIG(),
                             dash2015.participantesApenasDasSessoes(), dash2015.participantesApenasDasVideoEbserh(),
                             dash2015.participantesApenasDasVideoAulas()]

participantesPorCategoria2016 = [dash2016.participantesApenasDasBancas(), dash2016.participantesApenasDoSIG(),
                             dash2016.participantesApenasDasSessoes(), dash2016.participantesApenasDasVideoEbserh(),
                             dash2016.participantesApenasDasVideoAulas()]

participantesPorCategoria2017 = [dash2017.participantesApenasDasBancas(), dash2017.participantesApenasDoSIG(),
                             dash2017.participantesApenasDasSessoes(), dash2017.participantesApenasDasVideoEbserh(),
                             dash2017.participantesApenasDasVideoAulas()]

participantesPorCategoria2018 = [dash2018.participantesApenasDasBancas(), dash2018.participantesApenasDoSIG(),
                             dash2018.participantesApenasDasSessoes(), dash2018.participantesApenasDasVideoEbserh(),
                             dash2018.participantesApenasDasVideoAulas()]

def mesesDoAnoExtenso():
    mesesDoAnoPorExtenso = ["JANEIRO","FEVEREIRO","MARÇO","ABRIL","MAIO","JUNHO","JULHO","AGOSTO","SETEMBRO",
                            "OUTUBRO","NOVEMBRO","DEZEMBRO"]
    return mesesDoAnoPorExtenso

categorias = ["BANCAS EXAMINADORAS", "SIG's", "SESSÕES CLÍNICAS", "VIDEOCONFERÊNCIA-EBSERH", "GRAVAÇÃO DE VIDEOAULAS"]



fig = plt.figure(constrained_layout=True)
gs = GridSpec(2, 2, figure=fig)

ax1 = fig.add_subplot(gs[0, 0])
ax1.set_title("PARTICIPANTES 2015: " + str(dash2015.totalParticipantes()), fontsize = 25)
ax1.barh(categorias,participantesPorCategoria2015)
ax1.legend(fontsize = 18)

ax2 = fig.add_subplot(gs[0, 1])
ax2.set_title("PARTICIPANTES 2016: " + str(dash2016.totalParticipantes()), fontsize = 25)
ax2.barh(categorias,participantesPorCategoria2016, color ="grey")
ax2.legend(fontsize = 18)

ax3 = fig.add_subplot(gs[1, 0])
ax3.set_title("PARTICIPANTES 2017: " + str(dash2017.totalParticipantes()), fontsize = 25)
ax3.barh(categorias,participantesPorCategoria2017, color = "lightblue")
ax3.legend(fontsize = 18)

ax4 = fig.add_subplot(gs[1, 1])
ax4.set_title("PARTICIPANTES 2018: " + str(dash2018.totalParticipantes()), fontsize = 25)
ax4.barh(categorias,participantesPorCategoria2018, color = "red")
ax4.legend(fontsize = 18)

fig.suptitle("NÚMERO DE PARTICIPANTES DO NUTS DE 2015 A 2018", color = "black", fontsize = 55)
plt.show()