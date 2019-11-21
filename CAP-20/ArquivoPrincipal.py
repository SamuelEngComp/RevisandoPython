from ReceberArquivo import ReceberArquivoCSV
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np

dados2015 = ReceberArquivoCSV("atividade2015.csv")
dados2016 = ReceberArquivoCSV("atividadesNuts2016.csv")
dados2017 = ReceberArquivoCSV("atividadesNuts2017.csv")
dados2018 = ReceberArquivoCSV("ATIVIDADES NUTS 2018.csv")

dadosJaneiro = ReceberArquivoCSV("DashNuts2018/janeiro2018.csv")
dadosFevereiro = ReceberArquivoCSV("DashNuts2018/fevereiro2018.csv")
dadosMarco = ReceberArquivoCSV("DashNuts2018/marco2018.csv")
dadosAbril = ReceberArquivoCSV("DashNuts2018/abril2018.csv")
dadosMaio = ReceberArquivoCSV("DashNuts2018/maio2018.csv")
dadosJunho = ReceberArquivoCSV("DashNuts2018/junho2018.csv")
dadosJulho = ReceberArquivoCSV("DashNuts2018/julho2018.csv")
dadosAgosto = ReceberArquivoCSV("DashNuts2018/agosto2018.csv")
dadosSetembro = ReceberArquivoCSV("DashNuts2018/setembro2018.csv")
dadosOutubro = ReceberArquivoCSV("DashNuts2018/outubro2018.csv")
dadosNovembro = ReceberArquivoCSV("DashNuts2018/novembro2018.csv")
dadosDezembro = ReceberArquivoCSV("DashNuts2018/dezembro2018.csv")

ano = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
DadosAno2018 = [dadosJaneiro.totalAtividades(), dadosFevereiro.totalAtividades(), dadosMarco.totalAtividades(),
                dadosAbril.totalAtividades(), dadosMaio.totalAtividades(), dadosJunho.totalAtividades(),
                dadosJulho.totalAtividades(), dadosAgosto.totalAtividades(), dadosSetembro.totalAtividades(),
                dadosOutubro.totalAtividades(), dadosNovembro.totalAtividades(), dadosDezembro.totalAtividades()]

def somaAtividades2015():
    return dados2015.totalAtividades()

def somaAtividades2016():
    return dados2016.totalAtividades()

def somaAtividades2017():
    return dados2017.totalAtividades()

def somaAtividades2018():
    return dados2018.totalAtividades()

def somaTotalParticipantes():
    soma = [dados2018.totalParticipantes(), dados2017.totalParticipantes(), dados2016.totalParticipantes(), dados2015.totalParticipantes()]
    return soma

def somatorio():
    soma = [somaAtividades2018(), somaAtividades2017(), somaAtividades2016(), somaAtividades2015()]
    return soma

def somaAtividade2018():
    soma = 0
    for i in range(len(DadosAno2018)):
        soma += DadosAno2018[i]

    return soma

def exibirDados():
    print("Total atividades 2015: ", dados2015.totalAtividades())
    print("Total videoEBSERH 2015: ", dados2015.totalVideoConferenciaEBSERH())
    print("Total SIG 2015: ", dados2015.totalDeSIGs())
    print("Total BANCAS 2015: ", dados2015.totalDeBancas())
    print("Total participantes 2015: ", dados2015.totalParticipantes())


def exibirGraficoLinha(eixoX, eixoY, titulo):
    plt.title(titulo)
    plt.plot(eixoY, eixoX)
    # plt.legend()
    return plt.show()


def exibirGraficoBarras(eixoX, eixoY, titulo):
    plt.title(titulo)
    plt.ylabel("Valor")
    # plt.xlabel("Ano 2018")
    plt.plot(eixoY, eixoX, "r")
    plt.bar(eixoY, eixoX)
    plt.legend()
    return plt.show()


def exibirGraficoPizza(eixoX, eixoY,titulo):
    atividadeDestaque = (0,0,0,0,0,0,0,0,0,0,0,0)
    plt.title(titulo)
    plt.pie(eixoX,explode=atividadeDestaque,labels=eixoY, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.legend()
    return plt.show()


exibirGraficoLinha(DadosAno2018, ano, "Atividades - NUTS - 2018")
exibirGraficoBarras(DadosAno2018, ano, "Atividades - NUTS - 2018")
exibirGraficoPizza(DadosAno2018, ano, "Atividades 2018")



fig = plt.figure(constrained_layout=True)

gs = GridSpec(3, 3, figure=fig)

de2015Ate2018 = ["2018","2017","2016","2015"]
vd = [dados2018.totalDeVideoAulas(), dados2017.totalDeVideoAulas(), dados2016.totalDeVideoAulas(), dados2015.totalDeVideoAulas()]
sigs = [dados2018.totalDeSIGs(), dados2017.totalDeSIGs(), dados2016.totalDeSIGs(), dados2015.totalDeSIGs()]
sc = [dados2018.totalDeSessao(), dados2017.totalDeSessao(), dados2016.totalDeSessao(), dados2015.totalDeSessao()]
bancas = [dados2018.totalDeBancas(), dados2017.totalDeBancas(), dados2016.totalDeBancas(), dados2015.totalDeBancas()]
# comparativo = [vd, sigs, sc, bancas]
larguraDaBarra = 0.19
plt.figure(figsize=(12,7))
p1 = np.arange(len(vd))
p2 = [x + larguraDaBarra for x in p1]
p3 = [x + larguraDaBarra for x in p2]
p4 = [x + larguraDaBarra for x in p3]

# plt.bar(p1,vd,color="red",width=larguraDaBarra,label="Videoaulas")
# plt.bar(p2,sigs,color="blue",width=larguraDaBarra,label="SIG")
# plt.bar(p3,sc,color="orange",width=larguraDaBarra,label="Sessão Clinica")
# plt.bar(p4,bancas,color="grey",width=larguraDaBarra,label="Bancas")

# plt.xlabel("comparativo")
# plt.xticks([r + larguraDaBarra for r in range(len(p1))], de2015Ate2018)
# plt.ylabel("quantidade")
# plt.title("Comparativo de atividades")
# plt.legend()
# plt.show()

ax1 = fig.add_subplot(gs[0, :])
# ax1.set_title("teste 1")
ax1.plot(ano, DadosAno2018, "r")
ax1.bar(ano,DadosAno2018,width=0.32)
ax1.set_ylabel("qtd")
# ax1.set_xlabel("dias")

# identical to ax1 = plt.subplot(gs.new_subplotspec((0, 0), colspan=3))
ax2 = fig.add_subplot(gs[1, :-1])
ax2.set_title("Comparativo de atividades")
# ax2.bar(ano,DadosAno2018,width=0.32)
ax2.bar(p1,vd,color="red",width=larguraDaBarra,label="Videoaulas")
ax2.bar(p2,sigs,color="blue",width=larguraDaBarra,label="SIG")
ax2.bar(p3,sc,color="orange",width=larguraDaBarra,label="Sessão Clinica")
ax2.bar(p4,bancas,color="grey",width=larguraDaBarra,label="Bancas")

# ax2.xlabel("comparativo")
ax2.set_xticks([r + larguraDaBarra for r in range(len(p1))], de2015Ate2018)
# ax2.ylabel("quantidade")
# ax2.title("Comparativo de atividades")
ax2.set_ylabel("quantidade")
ax2.set_xlabel("comparativo")
ax2.legend()

ax3 = fig.add_subplot(gs[1:, -1])
ax3.set_title("teste 3")
# ax3.bar(x,y,width=0.32)
ax3.pie(DadosAno2018,labels = ano)
# ax3.set_ylabel("qtd")
# ax3.set_xlabel("dias")

ax4 = fig.add_subplot(gs[-1, 0])
ax4.set_title("Comparativo de Participantes")
ax4.barh(de2015Ate2018, somaTotalParticipantes(), color = "grey")
ax4.set_xlabel("Total de Participantes")
# ax4.set_xlabel("dias")



ax5 = fig.add_subplot(gs[-1, -2])
ax5.set_title("Comparativo Anual - NUTS")
ax5.barh(de2015Ate2018,somatorio(),color="red")
# ax5.set_ylabel("qtd")
ax5.set_xlabel("Quantidade de atividades por ano")

fig.suptitle("Atividades NUTS 2018")
plt.show()

exibirDados()
print("total de atividades 2018 - Planilha completa: ", somaAtividades2018())
print("total de atividades 2018 - Soma de cada mês: ", somaAtividade2018())