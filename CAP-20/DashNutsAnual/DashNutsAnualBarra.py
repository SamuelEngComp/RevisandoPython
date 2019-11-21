import plotly.graph_objects as go
from ReceberArquivo import ReceberArquivoCSV

import DashNuts2015.DashNuts2015 as ds2015
import DashNuts2016.DashNuts2016 as ds2016
import DashNuts2017.DashNuts2017 as ds2017
import DashNuts2018.DashNuts2018 as ds2018

dadosAnual2015 = ReceberArquivoCSV("atividade2015.csv")
dadosAnual2016 = ReceberArquivoCSV("atividadesNuts2016.csv")
dadosAnual2017 = ReceberArquivoCSV("atividadesNuts2017.csv")
dadosAnual2018 = ReceberArquivoCSV("ATIVIDADES NUTS 2018.csv")


meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
          'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

fig = go.Figure()
fig.add_trace(go.Bar(
    x=meses,
    y=[ds2015.totalAtivJaneiro(), ds2015.totalAtivFevereiro(), ds2015.totalAtivMarco(), ds2015.totalAtivAbril(),
       ds2015.totalAtivMaio(), ds2015.totalAtivJunho(), ds2015.totalAtivJulho(), ds2015.totalAtivAgosto(),
       ds2015.totalAtivSetembro(), ds2015.totalAtivOutubro(), ds2015.totalAtivNovembro(), ds2015.totalAtivDezembro()],
    name='Atividades Nuts 2015',
    marker_color='indianred'
))

fig.add_trace(go.Bar(
    x=meses,
    y=[ds2016.totalAtivJaneiro(), ds2016.totalAtivFevereiro(), ds2016.totalAtivMarco(), ds2016.totalAtivAbril(),
       ds2016.totalAtivMaio(), ds2016.totalAtivJunho(), ds2016.totalAtivJulho(), ds2016.totalAtivAgosto(),
       ds2016.totalAtivSetembro(), ds2016.totalAtivOutubro(), ds2016.totalAtivNovembro(), ds2016.totalAtivDezembro()],
    name='Atividades Nuts 2016',
    marker_color='lightsalmon'
))

fig.add_trace(go.Bar(
    x=meses,
    y=[ds2017.totalAtivJaneiro(), ds2017.totalAtivFevereiro(), ds2017.totalAtivMarco(), ds2017.totalAtivAbril(),
       ds2017.totalAtivMaio(), ds2017.totalAtivJunho(), ds2017.totalAtivJulho(), ds2017.totalAtivAgosto(),
       ds2017.totalAtivSetembro(), ds2017.totalAtivOutubro(), ds2017.totalAtivNovembro(), ds2017.totalAtivDezembro()],
    name='Atividades Nuts 2017',
    marker_color='blue'
))

fig.add_trace(go.Bar(
    x=meses,
    y=[ds2018.totalAtivJaneiro(), ds2018.totalAtivFevereiro(), ds2018.totalAtivMarco(), ds2018.totalAtivAbril(),
       ds2018.totalAtivMaio(), ds2018.totalAtivJunho(), ds2018.totalAtivJulho(), ds2018.totalAtivAgosto(),
       ds2018.totalAtivSetembro(), ds2018.totalAtivOutubro(), ds2018.totalAtivNovembro(), ds2018.totalAtivDezembro()],
    name='Atividades Nuts 2018',
    marker_color='grey'
))

# Here we modify the tickangle of the xaxis, resulting in rotated labels.
fig.update_layout(barmode='group', xaxis_tickangle=-45, title_text = "Painel de Atividades")
fig.show()