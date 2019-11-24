import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from ReceberArquivo import ReceberArquivoCSV

dadosTempoBancas2015 = ReceberArquivoCSV("atividade2015.csv")
dadosTempoBancas2016 = ReceberArquivoCSV("atividadesNuts2016.csv")
dadosTempoBancas2017 = ReceberArquivoCSV("atividadesNuts2017.csv")
dadosTempoBancas2018 = ReceberArquivoCSV("ATIVIDADES NUTS 2018.csv")

print("Tempo bancas: ", dadosTempoBancas2015.tempoBancasNovo())
print("Tempo bancas: ", dadosTempoBancas2016.tempoBancasNovo())
print("Tempo bancas: ", dadosTempoBancas2017.tempoBancasNovo())
print("Tempo bancas: ", dadosTempoBancas2018.tempoBancasNovo())

tempoDasBancas = [dadosTempoBancas2015.tempoBancasNovo(), dadosTempoBancas2016.tempoBancasNovo(),
                  dadosTempoBancas2017.tempoBancasNovo(), dadosTempoBancas2018.tempoBancasNovo()]

from DashNuts2015.DashNuts2015 import totalBancasExaminadorasPorMes as tbe2015, participantesPorCategoria as parti2015

from DashNuts2016.DashNuts2016 import totalBancasExaminadorasPorMes as tbe2016, participantesPorCategoria as parti2016

from DashNuts2017.DashNuts2017 import totalBancasExaminadorasPorMes as tbe2017, participantesPorCategoria as parti2017

from DashNuts2018.DashNuts2018 import totalBancasExaminadorasPorMes as tbe2018, participantesPorCategoria as parti2018

print("TOTAL 2015: ", tbe2015(), "Participantes: ", parti2015[0] )
print("TOTAL 2016: ", tbe2016(), "Participantes: ", parti2016[0])
print("TOTAL 2017: ", tbe2017(), "Participantes: ", parti2017[0])
print("TOTAL 2018: ", tbe2018(), "Participantes: ", parti2018[0])

vetorBancas2015 = tbe2015().copy()
vetorBancas2016 = tbe2016().copy()
vetorBancas2017 = tbe2017().copy()
vetorBancas2018 = tbe2018().copy()

def somaBancas2015():
    soma = 0
    for i in range(len(vetorBancas2015)):
        soma += vetorBancas2015[i]

    return soma

def somaBancas2016():
    soma = 0
    for i in range(len(vetorBancas2016)):
        soma += vetorBancas2016[i]

    return soma

def somaBancas2017():
    soma = 0
    for i in range(len(vetorBancas2017)):
        soma += vetorBancas2017[i]

    return soma

def somaBancas2018():
    soma = 0
    for i in range(len(vetorBancas2018)):
        soma += vetorBancas2018[i]

    return soma

print("Soma bancas 2015: ", somaBancas2015())
print("Soma bancas 2016: ", somaBancas2016())
print("Soma bancas 2017: ", somaBancas2017())
print("Soma bancas 2018: ", somaBancas2018())



######################################################################################################################

labels = '2015', '2016', '2017', '2018'
sizes = [somaBancas2015(), somaBancas2016(), somaBancas2017(), somaBancas2018()]
participantesVetor = [parti2015[0], parti2016[0], parti2017[0], parti2018[0]]
explode = (0, 0, 0, 0.1)

fig = plt.figure(constrained_layout=True)
gs = GridSpec(2, 2, figure=fig)

anosComparados = ["2015","2016","2017","2018"]

ax1 = fig.add_subplot(gs[0, 0])
ax1.set_title("BANCAS EXAMINADORAS: " + str((sizes[0] + sizes[1] + sizes[2] + sizes[3])), fontsize = 25)
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.legend(fontsize = 12)

ax2 = fig.add_subplot(gs[0, 1])
ax2.set_title("PÚBLICO DAS BANCAS: " + str((parti2015[0] + parti2016[0] + parti2017[0] + parti2018[0])), fontsize = 25)
ax2.plot(anosComparados, participantesVetor, color = "red", marker = "x", label = "BANCAS")
ax2.bar(anosComparados, participantesVetor,width=0.32)
ax2.legend(fontsize = 18)

ax3 = fig.add_subplot(gs[1, 0])
ax3.set_title("HORAS DE ATIVIDADE: " + str(round((tempoDasBancas[0]+tempoDasBancas[1]+tempoDasBancas[2]+tempoDasBancas[3]),2)),
              fontsize = 25)
ax3.barh(anosComparados, tempoDasBancas, color ="grey")
# ax3.legend(fontsize = 18)

ax4 = fig.add_subplot(gs[1, 1])
ax4.set_title("VALOR ECONOMIZADO COM DIÁRIAS E PASSAGENS - NUTS", fontsize = 25)

###########################################################3
def format_axes():
    ax4.text(0.5, 0.5, "R$ 341.164,92" , va="center", ha="center", fontsize = 125, color = "blue")
    ax4.tick_params(labelbottom=False, labelleft=False)


fig.suptitle("BANCAS REALIZADAS NO NUTS DE 2015 A 2018", color = "black", fontsize = 55)
format_axes()
plt.show()