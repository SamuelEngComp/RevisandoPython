from ReceberArquivo import ReceberArquivoCSV
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np

dadosDoAno = ReceberArquivoCSV("atividade2015.csv")

dadosJan = ReceberArquivoCSV("jan2015.csv")
dadosFev = ReceberArquivoCSV("fev2015.csv")
dadosMar = ReceberArquivoCSV("mar2015.csv")
dadosAbr = ReceberArquivoCSV("abr2015.csv")
dadosMai = ReceberArquivoCSV("mai2015.csv")
dadosJun = ReceberArquivoCSV("jun2015.csv")
dadosJul = ReceberArquivoCSV("jul2015.csv")
dadosAgo = ReceberArquivoCSV("ago2015.csv")
dadosSet = ReceberArquivoCSV("set2015.csv")
dadosOut = ReceberArquivoCSV("out2015.csv")
dadosNov = ReceberArquivoCSV("nov2015.csv")
dadosDez = ReceberArquivoCSV("dez2015.csv")


def totalParticipantesJan():
    return dadosJan.totalParticipantes()

def totalParticipantesFev():
    return dadosFev.totalParticipantes()

def totalParticipantesMar():
    return dadosMar.totalParticipantes()

def totalParticipantesAbr():
    return dadosAbr.totalParticipantes()

def totalParticipantesMai():
    return dadosMai.totalParticipantes()

def totalParticipantesJun():
    return dadosJun.totalParticipantes()

def totalParticipantesJul():
    return dadosJul.totalParticipantes()

def totalParticipantesAgo():
    return dadosAgo.totalParticipantes()

def totalParticipantesSet():
    return dadosSet.totalParticipantes()

def totalParticipantesOut():
    return dadosOut.totalParticipantes()

def totalParticipantesNov():
    return dadosNov.totalParticipantes()

def totalParticipantesDez():
    return dadosDez.totalParticipantes()


def totalParticipantes():
    return dadosDoAno.totalParticipantes()

def totalHoras():
    tempoEmMinutos = dadosDoAno.totalTempoMes()
    return round(tempoEmMinutos/60, 0)

def totalAtivJaneiro():
    return dadosJan.totalAtividades()


def totalAtivFevereiro():
    return dadosFev.totalAtividades()


def totalAtivMarco():
    return dadosMar.totalAtividades()


def totalAtivAbril():
    return dadosAbr.totalAtividades()


def totalAtivMaio():
    return dadosMai.totalAtividades()


def totalAtivJunho():
    return dadosJun.totalAtividades()


def totalAtivJulho():
    return dadosJul.totalAtividades()


def totalAtivAgosto():
    return dadosAgo.totalAtividades()


def totalAtivSetembro():
    return dadosSet.totalAtividades()


def totalAtivOutubro():
    return dadosOut.totalAtividades()


def totalAtivNovembro():
    return dadosNov.totalAtividades()


def totalAtivDezembro():
    return dadosDez.totalAtividades()


def somaAtividades2015():
    return dadosDoAno.totalAtividades()


def mesesDoAnoAbreviado():
    mesesDoAnoAbreviados = ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]
    return mesesDoAnoAbreviados


def mesesDoAnoExtenso():
    mesesDoAnoPorExtenso = ["JANEIRO","FEVEREIRO","MARÇO","ABRIL","MAIO","JUNHO","JULHO","AGOSTO","SETEMBRO",
                            "OUTUBRO","NOVEMBRO","DEZEMBRO"]
    return mesesDoAnoPorExtenso


def somaMeses():
    return (totalAtivJaneiro()+totalAtivFevereiro()+totalAtivMarco()+totalAtivAbril()+
            totalAtivMaio()+totalAtivJunho()+totalAtivJulho()+totalAtivAgosto()+totalAtivSetembro()+
            totalAtivOutubro()+totalAtivNovembro()+totalAtivDezembro())


def totalDeAtividadeDeCadaMes():
    atividades = [totalAtivJaneiro(), totalAtivFevereiro(), totalAtivMarco(), totalAtivAbril(),
                  totalAtivMaio(), totalAtivJunho(), totalAtivJulho(), totalAtivAgosto(),
                  totalAtivSetembro(), totalAtivOutubro(), totalAtivNovembro(), totalAtivDezembro()]
    return atividades


def totalDeParticipantesDeCadaMes():
    participantes = [dadosJan.totalParticipantes(), dadosFev.totalParticipantes(), dadosMar.totalParticipantes(),
                     dadosAbr.totalParticipantes(), dadosMai.totalParticipantes(), dadosJun.totalParticipantes(),
                     dadosJul.totalParticipantes(), dadosAgo.totalParticipantes(), dadosSet.totalParticipantes(),
                     dadosOut.totalParticipantes(), dadosNov.totalParticipantes(), dadosDez.totalParticipantes()]
    return participantes


def totalDeHorasDeCadaMes():
    horas = [round(dadosJan.totalTempoMes()/60, 2), round(dadosFev.totalTempoMes()/60, 2), round(dadosMar.totalTempoMes()/60, 2),
             round(dadosAbr.totalTempoMes()/60, 2), round(dadosMai.totalTempoMes()/60, 2), round(dadosJun.totalTempoMes()/60, 2),
             round(dadosJul.totalTempoMes()/60, 2), round(dadosAgo.totalTempoMes()/60, 2), round(dadosSet.totalTempoMes()/60, 2),
             round(dadosOut.totalTempoMes()/60, 2), round(dadosNov.totalTempoMes()/ 60, 2), round(dadosDez.totalTempoMes()/60, 2)]

    return horas


def totalDeSIGPorMes():
    sigs = [dadosJan.totalDeSIGs(), dadosFev.totalDeSIGs(), dadosMar.totalDeSIGs(), dadosAbr.totalDeSIGs(), dadosMai.totalDeSIGs(),
            dadosJun.totalDeSIGs(), dadosJul.totalDeSIGs(), dadosAgo.totalDeSIGs(), dadosSet.totalDeSIGs(), dadosOut.totalDeSIGs(),
            dadosNov.totalDeSIGs(), dadosDez.totalDeSIGs()]
    return sigs


def totalDeVideoEbserhPorMes():
    videoEbserh = [dadosJan.totalVideoConferenciaEBSERH(), dadosFev.totalVideoConferenciaEBSERH(), dadosMar.totalVideoConferenciaEBSERH(),
                   dadosAbr.totalVideoConferenciaEBSERH(), dadosMai.totalVideoConferenciaEBSERH(), dadosJun.totalVideoConferenciaEBSERH(),
                   dadosJul.totalVideoConferenciaEBSERH(), dadosAgo.totalVideoConferenciaEBSERH(), dadosSet.totalVideoConferenciaEBSERH(),
                   dadosOut.totalVideoConferenciaEBSERH(), dadosNov.totalVideoConferenciaEBSERH(), dadosDez.totalVideoConferenciaEBSERH()]
    return videoEbserh

def totalVideoAulasPorMes():
    videoAulas = [dadosJan.totalDeVideoAulas(), dadosFev.totalDeVideoAulas(), dadosMar.totalDeVideoAulas(), dadosAbr.totalDeVideoAulas(),
                  dadosMai.totalDeVideoAulas(), dadosJun.totalDeVideoAulas(), dadosJul.totalDeVideoAulas(), dadosAgo.totalDeVideoAulas(),
                  dadosSet.totalDeVideoAulas(), dadosOut.totalDeVideoAulas(), dadosNov.totalDeVideoAulas(), dadosDez.totalDeVideoAulas()]
    return videoAulas

def totalSessaoClinicaPorMes():
    sessoes = [dadosJan.totalDeSessao(), dadosFev.totalDeSessao(), dadosMar.totalDeSessao(), dadosAbr.totalDeSessao(),
               dadosMai.totalDeSessao(), dadosJun.totalDeSessao(), dadosJul.totalDeSessao(), dadosAgo.totalDeSessao(),
               dadosSet.totalDeSessao(), dadosOut.totalDeSessao(), dadosNov.totalDeSessao(), dadosDez.totalDeSessao()]
    return sessoes


def totalBancasExaminadorasPorMes():
    bancasExaminadoras = [dadosJan.totalDeBancas(), dadosFev.totalDeBancas(), dadosMar.totalDeBancas(), dadosAbr.totalDeBancas(),
                          dadosMai.totalDeBancas(), dadosJun.totalDeBancas(), dadosJul.totalDeBancas(), dadosAgo.totalDeBancas(),
                          dadosSet.totalDeBancas(), dadosOut.totalDeBancas(), dadosNov.totalDeBancas(), dadosDez.totalDeBancas()]
    return bancasExaminadoras


def somaSessoesClinicas():
    soma = 0
    sessoes = totalSessaoClinicaPorMes()
    for i in range(len(sessoes)):
        soma += sessoes[i]

    return soma


def somaBancas():
    soma = 0
    bancas = totalBancasExaminadorasPorMes()
    for i in range(len(bancas)):
        soma += bancas[i]

    return soma


def somaSigs():
    soma = 0
    sigs = totalDeSIGPorMes()
    for i in range(len(sigs)):
        soma += sigs[i]

    return soma

def somaVideoAulas():
    soma = 0
    videoAulas = totalVideoAulasPorMes()
    for i in range(len(videoAulas)):
        soma += videoAulas[i]

    return soma

def somaVCEbserh():
    soma = 0
    vcEbserh = totalDeVideoEbserhPorMes()
    for i in range(len(vcEbserh)):
        soma += vcEbserh[i]

    return soma

def exibirDados():
    tempoTotalEmMinutos = dadosDoAno.totalTempoMes()
    # print("Total atividades 2015: ", dadosDoAno.totalAtividades())
    # print("Total videoEBSERH 2015: ", dadosDoAno.totalVideoConferenciaEBSERH())
    # print("Total SIG 2015: ", dadosDoAno.totalDeSIGs())
    # print("Total BANCAS 2015: ", dadosDoAno.totalDeBancas())
    # print("Total participantes 2015: ", dadosDoAno.totalParticipantes())
    print("Total em horas: ", round(tempoTotalEmMinutos/60, 2))


print(totalAtivJaneiro())
print(totalAtivFevereiro())
print(totalAtivMarco())
print(totalAtivAbril())
print(totalAtivMaio())
print(totalAtivJunho())
print(totalAtivJulho())
print(totalAtivAgosto())
print(totalAtivSetembro())
print(totalAtivOutubro())
print(totalAtivNovembro())
print(totalAtivDezembro())
print("soma: ", somaMeses())
print("|||||||||||||||||||||||||||||||||||||")
print(somaAtividades2015())
print("Total de horas em cada mes: ", totalDeHorasDeCadaMes())
print("||||||||||||##############||||||||||||||||")
exibirDados()

#
fig = plt.figure(constrained_layout=True)
gs = GridSpec(3, 3, figure=fig)

#
ax1 = fig.add_subplot(gs[0, :])
ax1.set_title("TOTAL DE - " + str(somaMeses()) + " - ATIVIDADE", fontsize = 25)
ax1.plot(mesesDoAnoExtenso(), totalDeSIGPorMes(), color = "red", marker = "x", label = "SIG")
ax1.plot(mesesDoAnoExtenso(), totalBancasExaminadorasPorMes(), color = "grey", marker = "*", label = "BANCAS")
ax1.plot(mesesDoAnoExtenso(), totalVideoAulasPorMes(),color = "green", marker = "o", label = "VIDEOAULAS")
ax1.plot(mesesDoAnoExtenso(), totalDeVideoEbserhPorMes(),color = "orange", marker = "x", label = "EBSERH")
ax1.plot(mesesDoAnoExtenso(), totalSessaoClinicaPorMes(),color = "black", marker = "o", label = "SESSÃO CLÍNICA")
ax1.bar(mesesDoAnoExtenso(),totalDeAtividadeDeCadaMes(),width=0.32)
ax1.legend(fontsize = 20)
# ax1.set_ylabel("QUANTIDADE")
# ax1.set_xlabel("PERÍODO")
#
# # identical to ax1 = plt.subplot(gs.new_subplotspec((0, 0), colspan=3))

######################################################################################
categorias = ["BANCAS EXAMINADORAS", "SIG's", "SESSÕES CLÍNICAS", "VIDEOCONFERÊNCIA-EBSERH", "GRAVAÇÃO DE VIDEOAULAS"]

# resultados = {
#     "Janeiro":[dadosJan.totalDeBancas(), dadosJan.totalDeSIGs(), dadosJan.totalDeSessao(), dadosJan.totalVideoConferenciaEBSERH(), dadosJan.totalDeVideoAulas()],
#     "Fevereiro":[dadosFev.totalDeBancas(), dadosFev.totalDeSIGs(), dadosFev.totalDeSessao(), dadosFev.totalVideoConferenciaEBSERH(), dadosFev.totalDeVideoAulas()],
#     "Março":[dadosMar.totalDeBancas(), dadosMar.totalDeSIGs(), dadosMar.totalDeSessao(), dadosMar.totalVideoConferenciaEBSERH(), dadosMar.totalDeVideoAulas()],
#     "Abril":[dadosAbr.totalDeBancas(), dadosAbr.totalDeSIGs(), dadosAbr.totalDeSessao(), dadosAbr.totalVideoConferenciaEBSERH(), dadosAbr.totalDeVideoAulas()],
#     "Maio":[dadosMai.totalDeBancas(), dadosMai.totalDeSIGs(), dadosMai.totalDeSessao(), dadosMai.totalVideoConferenciaEBSERH(), dadosMai.totalDeVideoAulas()],
#     "Junho":[dadosJun.totalDeBancas(), dadosJun.totalDeSIGs(), dadosJun.totalDeSessao(), dadosJun.totalVideoConferenciaEBSERH(), dadosJun.totalDeVideoAulas()],
#     "Julho":[dadosJul.totalDeBancas(), dadosJul.totalDeSIGs(), dadosJul.totalDeSessao(), dadosJul.totalVideoConferenciaEBSERH(), dadosJul.totalDeVideoAulas()],
#     "Agosto":[dadosAgo.totalDeBancas(), dadosAgo.totalDeSIGs(), dadosAgo.totalDeSessao(), dadosAgo.totalVideoConferenciaEBSERH(), dadosAgo.totalDeVideoAulas()],
#     "Setembro":[dadosSet.totalDeBancas(), dadosSet.totalDeSIGs(), dadosSet.totalDeSessao(), dadosSet.totalVideoConferenciaEBSERH(), dadosSet.totalDeVideoAulas()],
#     "Outubro":[dadosOut.totalDeBancas(), dadosOut.totalDeSIGs(), dadosOut.totalDeSessao(), dadosOut.totalVideoConferenciaEBSERH(), dadosOut.totalDeVideoAulas()],
#     "Novembro":[dadosNov.totalDeBancas(), dadosNov.totalDeSIGs(), dadosNov.totalDeSessao(), dadosNov.totalVideoConferenciaEBSERH(), dadosNov.totalDeVideoAulas()],
#     "Dezembro":[dadosDez.totalDeBancas(), dadosDez.totalDeSIGs(), dadosDez.totalDeSessao(), dadosDez.totalVideoConferenciaEBSERH(), dadosDez.totalDeVideoAulas()]
# }

# def survey(resultados, categorias):
#
#     labels = list(resultados.keys())
#     data = np.array(list(resultados.values()))
#     data_cum = data.cumsum(axis=1)
#     category_colors = plt.get_cmap('RdYlGn')(
#         np.linspace(0.15, 0.85, data.shape[1]))
#
#     fig, ax = plt.subplots(figsize=(9.2, 5))
#     ax.invert_yaxis()
#     ax.xaxis.set_visible(False)
#     ax.set_xlim(0, np.sum(data, axis=1).max())
#
#     for i, (colname, color) in enumerate(zip(categorias, category_colors)):
#         widths = data[:, i]
#         starts = data_cum[:, i] - widths
#         ax.barh(labels, widths, left=starts, height=0.5,
#                 label=colname, color=color)
#         xcenters = starts + widths / 2
#
#         r, g, b, _ = color
#         text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
#         for y, (x, c) in enumerate(zip(xcenters, widths)):
#             ax.text(x, y, str(int(c)), ha='center', va='center',
#                     color=text_color)
#     ax.legend(ncol=len(categorias), bbox_to_anchor=(0, 1),
#               loc='lower left', fontsize='small')
#
#     return fig, ax


# survey(resultados, categorias)
# plt.show()
######################################################################################



participantesPorCategoria = [dadosDoAno.participantesApenasDasBancas(), dadosDoAno.participantesApenasDoSIG(),
                             dadosDoAno.participantesApenasDasSessoes(), dadosDoAno.participantesApenasDasVideoEbserh(),
                             dadosDoAno.participantesApenasDasVideoAulas()]

ax2 = fig.add_subplot(gs[1, :-1])
ax2.set_title("PARTICIPANTES POR ATIVIDADE", fontsize = 25)
ax2.barh(categorias, participantesPorCategoria, color = "orange")
# ax2.set_ylabel("ATIVIDADE")
# ax2.set_xlabel("QUANTIDADE")
# ax2.legend("Total de participantes por atividade")
#
ax3 = fig.add_subplot(gs[1:, -1])
explode = (0,0,0.1,0,0)
# ax3.set_title("Ativ")
# # ax3.bar(x,y,width=0.32)
valoresCategorias = [dadosDoAno.totalDeBancas(), dadosDoAno.totalDeSIGs(), dadosDoAno.totalDeSessao(), dadosDoAno.totalVideoConferenciaEBSERH(), dadosDoAno.totalDeVideoAulas()]
ax3.pie(valoresCategorias, explode = explode,labels = categorias, autopct='%1.1f%%', shadow=True, startangle=90)
# ax3.axis('equal')
ax3.legend(fontsize = 20)
# # ax3.set_ylabel("qtd")
# # ax3.set_xlabel("dias")
#Participantes = 2313

ax4 = fig.add_subplot(gs[-1, 0])
ax4.set_title("TOTAL DE - "+ str(totalParticipantes()) + " - PARTICIPANTES", fontsize = 25)
ax4.barh(mesesDoAnoExtenso(), totalDeParticipantesDeCadaMes(), color = "grey")
ax4.set_xlabel("QUANTIDADE DE PARTICIPANTES")
#
# total de horas: 502
ax5 = fig.add_subplot(gs[-1, -2])
ax5.set_title("TOTAL DE - " + str(totalHoras()) + " - HORAS DE ATIVIDADE", fontsize = 25)
ax5.barh(mesesDoAnoExtenso(),totalDeHorasDeCadaMes(),color="red")
ax5.set_xlabel("QUANTIDADE DE HORAS")


#
fig.suptitle("ATIVIDADES DO NUTS EM 2015", color = "black", fontsize = 55)
plt.show()

print("cada mes: ", totalDeParticipantesDeCadaMes())
print("total no ano: ", dadosDoAno.totalParticipantes())