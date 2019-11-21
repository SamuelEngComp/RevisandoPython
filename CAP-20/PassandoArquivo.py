import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
from ReceberArquivo import ReceberArquivoCSV

class PassandoPlanilhaCSV():

    def __init__(self):
        dadosJaneiro = ReceberArquivoCSV("janeiro2018.csv")
        dadosFevereiro = ReceberArquivoCSV("fevereiro2018.csv")
        dadosMarco = ReceberArquivoCSV("marco2018.csv")
        dadosAbril = ReceberArquivoCSV("abril2018.csv")
        dadosMaio = ReceberArquivoCSV("maio2018.csv")
        dadosJunho = ReceberArquivoCSV("junho2018.csv")
        dadosJulho = ReceberArquivoCSV("julho2018.csv")
        dadosAgosto = ReceberArquivoCSV("agosto2018.csv")
        dadosSetembro = ReceberArquivoCSV("setembro2018.csv")
        dadosOutubro = ReceberArquivoCSV("outubro2018.csv")
        dadosNovembro = ReceberArquivoCSV("novembro2018.csv")
        dadosDezembro = ReceberArquivoCSV("dezembro2018.csv")

        ano = ["Jan: ", dadosJaneiro.totalDeSIGs(),"fev: ", dadosFevereiro.totalDeSIGs(),
               "mar: ", dadosMarco.totalDeSIGs(),"abr: ", dadosAbril.totalDeSIGs(),
                "mai: ", dadosMaio.totalDeSIGs(),"jun: ", dadosJunho.totalDeSIGs(),
               "jul: ", dadosJulho.totalDeSIGs(),"ago: ", dadosAgosto.totalDeSIGs(),
               "set: ", dadosSetembro.totalDeSIGs(),"out: ", dadosOutubro.totalDeSIGs(),
               "nov: ", dadosNovembro.totalDeSIGs(),"dez: ", dadosDezembro.totalDeSIGs()]



        ano2018 = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
        valoresSIG = [dadosJaneiro.totalDeSIGs(),dadosFevereiro.totalDeSIGs(),dadosMarco.totalDeSIGs(),
                   dadosAbril.totalDeSIGs(),dadosMaio.totalDeSIGs(),dadosJunho.totalDeSIGs(),
                   dadosJulho.totalDeSIGs(),dadosAgosto.totalDeSIGs(),dadosSetembro.totalDeSIGs(),
                   dadosOutubro.totalDeSIGs(),dadosNovembro.totalDeSIGs(),dadosDezembro.totalDeSIGs()]

        # print(ano2018)
        # print(valoresSIG)
        valoresSessao = [dadosJaneiro.totalDeSessao(), dadosFevereiro.totalDeSessao(),dadosMarco.totalDeSessao(),
                          dadosAbril.totalDeSessao(),dadosMaio.totalDeSessao(),dadosJunho.totalDeSessao(),dadosJulho.totalDeSessao(),
                          dadosAgosto.totalDeSessao(),dadosSetembro.totalDeSessao(),dadosOutubro.totalDeSessao(),dadosNovembro.totalDeSessao(),
                          dadosDezembro.totalDeSessao()]
        #

        valoresVideoAulas = [dadosJaneiro.totalDeVideoAulas(), dadosFevereiro.totalDeVideoAulas(), dadosMarco.totalDeVideoAulas(),
                             dadosAbril.totalDeVideoAulas(), dadosMaio.totalDeVideoAulas(), dadosJunho.totalDeVideoAulas(),
                             dadosJulho.totalDeVideoAulas(), dadosAgosto.totalDeVideoAulas(), dadosSetembro.totalDeVideoAulas(),
                             dadosOutubro.totalDeVideoAulas(), dadosNovembro.totalDeVideoAulas(), dadosDezembro.totalDeVideoAulas()]
        sig = valoresSIG
        valoresSessaoClinica = valoresSessao

        #
        x = np.arange(len(ano2018))
        width = 0.35
        #
        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/2, sig, width, label='SIG')
        rects2 = ax.bar(x + width/2, valoresSessaoClinica, width, label='SessãoClinica')
        # rects3 = ax.bar(x + width/2, valoresVideoAulas, width, label='Videoaula')
        #
        # # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Quantidades')
        ax.set_title('Comparativo SIG e Sessão - 2018')
        ax.set_xticks(x)
        ax.set_xticklabels(ano2018)
        ax.legend()
        #

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
        # autolabel(rects3)

        fig.tight_layout()

        plt.show()
