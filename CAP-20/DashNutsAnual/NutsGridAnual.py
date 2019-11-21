import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from DashNuts2015.DashNuts2015 import somaMeses as sm2015, totalDeSIGPorMes as ts2015, totalBancasExaminadorasPorMes as tbe2015, \
    totalVideoAulasPorMes as tva2015, totalDeVideoEbserhPorMes as tve2015, totalSessaoClinicaPorMes as tsc2015, \
    totalDeAtividadeDeCadaMes as tatividade2015

from DashNuts2016.DashNuts2016 import somaMeses as sm2016, totalDeSIGPorMes as ts2016, totalBancasExaminadorasPorMes as tbe2016, \
    totalVideoAulasPorMes as tva2016, totalDeVideoEbserhPorMes as tve2016, totalSessaoClinicaPorMes as tsc2016, \
    totalDeAtividadeDeCadaMes as tatividade2016

from DashNuts2017.DashNuts2017 import somaMeses as sm2017, totalDeSIGPorMes as ts2017, totalBancasExaminadorasPorMes as tbe2017, \
    totalVideoAulasPorMes as tva2017, totalDeVideoEbserhPorMes as tve2017, totalSessaoClinicaPorMes as tsc2017, \
    totalDeAtividadeDeCadaMes as tatividade2017

from DashNuts2018.DashNuts2018 import somaMeses as sm2018, totalDeSIGPorMes as ts2018, totalBancasExaminadorasPorMes as tbe2018, \
    totalVideoAulasPorMes as tva2018, totalDeVideoEbserhPorMes as tve2018, totalSessaoClinicaPorMes as tsc2018, \
    totalDeAtividadeDeCadaMes as tatividade2018


def mesesDoAnoExtenso():
    mesesDoAnoPorExtenso = ["JANEIRO","FEVEREIRO","MARÇO","ABRIL","MAIO","JUNHO","JULHO","AGOSTO","SETEMBRO",
                            "OUTUBRO","NOVEMBRO","DEZEMBRO"]
    return mesesDoAnoPorExtenso

fig = plt.figure(constrained_layout=True)
gs = GridSpec(2, 2, figure=fig)

ax1 = fig.add_subplot(gs[0, 0])
ax1.set_title("ATIVIDADES 2015: " + str(sm2015()), fontsize = 25)
ax1.plot(mesesDoAnoExtenso(), ts2015(), color = "red", marker = "x", label = "SIG")
ax1.plot(mesesDoAnoExtenso(), tbe2015(), color = "grey", marker = "*", label = "BANCAS")
ax1.plot(mesesDoAnoExtenso(), tva2015(),color = "green", marker = "o", label = "VIDEOAULAS")
ax1.plot(mesesDoAnoExtenso(), tve2015(),color = "orange", marker = "x", label = "EBSERH")
ax1.plot(mesesDoAnoExtenso(), tsc2015(),color = "black", marker = "o", label = "SESSÃO CLÍNICA")
ax1.bar(mesesDoAnoExtenso(),tatividade2015(),width=0.32)
ax1.legend(fontsize = 18)

ax2 = fig.add_subplot(gs[0, 1])
ax2.set_title("ATIVIDADES 2016: " + str(sm2016()), fontsize = 25)
ax2.plot(mesesDoAnoExtenso(), ts2016(), color = "red", marker = "x", label = "SIG")
ax2.plot(mesesDoAnoExtenso(), tbe2016(), color = "blue", marker = "*", label = "BANCAS")
ax2.plot(mesesDoAnoExtenso(), tva2016(),color = "green", marker = "o", label = "VIDEOAULAS")
ax2.plot(mesesDoAnoExtenso(), tve2016(),color = "orange", marker = "x", label = "EBSERH")
ax2.plot(mesesDoAnoExtenso(), tsc2016(),color = "black", marker = "o", label = "SESSÃO CLÍNICA")
ax2.bar(mesesDoAnoExtenso(),tatividade2016(),width=0.32, color ="grey")
ax2.legend(fontsize = 18)

ax3 = fig.add_subplot(gs[1, 0])
ax3.set_title("ATIVIDADES 2017: " + str(sm2017()), fontsize = 25)
ax3.plot(mesesDoAnoExtenso(), ts2017(), color = "red", marker = "x", label = "SIG")
ax3.plot(mesesDoAnoExtenso(), tbe2017(), color = "blue", marker = "*", label = "BANCAS")
ax3.plot(mesesDoAnoExtenso(), tva2017(),color = "green", marker = "o", label = "VIDEOAULAS")
ax3.plot(mesesDoAnoExtenso(), tve2017(),color = "orange", marker = "x", label = "EBSERH")
ax3.plot(mesesDoAnoExtenso(), tsc2017(),color = "black", marker = "o", label = "SESSÃO CLÍNICA")
ax3.bar(mesesDoAnoExtenso(),tatividade2017(),width=0.32, color = "lightblue")
ax3.legend(fontsize = 18)

ax4 = fig.add_subplot(gs[1, 1])
ax4.set_title("ATIVIDADES 2018: " + str(sm2018()), fontsize = 25)
ax4.plot(mesesDoAnoExtenso(), ts2018(), color = "blue", marker = "x", label = "SIG")
ax4.plot(mesesDoAnoExtenso(), tbe2018(), color = "grey", marker = "*", label = "BANCAS")
ax4.plot(mesesDoAnoExtenso(), tva2018(),color = "green", marker = "o", label = "VIDEOAULAS")
ax4.plot(mesesDoAnoExtenso(), tve2018(),color = "orange", marker = "x", label = "EBSERH")
ax4.plot(mesesDoAnoExtenso(), tsc2018(),color = "black", marker = "o", label = "SESSÃO CLÍNICA")
ax4.bar(mesesDoAnoExtenso(),tatividade2018(),width=0.32, color = "red")
ax4.legend(fontsize = 18)

fig.suptitle("ATIVIDADES DO NUTS DE 2015 A 2018", color = "black", fontsize = 55)
plt.show()