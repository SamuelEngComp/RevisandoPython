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
    y=[ds2015.totalParticipantesJan(), ds2015.totalParticipantesFev(), ds2015.totalParticipantesMar(),
       ds2015.totalParticipantesAbr(), ds2015.totalParticipantesMai(), ds2015.totalParticipantesJun(),
       ds2015.totalParticipantesJul(), ds2015.totalParticipantesAgo(), ds2015.totalParticipantesSet(),
       ds2015.totalParticipantesOut(), ds2015.totalParticipantesNov(), ds2015.totalParticipantesDez()],
    name='Participantes 2015',
    marker_color='indianred'
))

fig.add_trace(go.Bar(
    x=meses,
    y=[ds2016.totalParticipantesJan(), ds2016.totalParticipantesFev(), ds2016.totalParticipantesMar(),
       ds2016.totalParticipantesAbr(), ds2016.totalParticipantesMai(), ds2016.totalParticipantesJun(),
       ds2016.totalParticipantesJul(), ds2016.totalParticipantesAgo(), ds2016.totalParticipantesSet(),
       ds2016.totalParticipantesOut(), ds2016.totalParticipantesNov(), ds2016.totalParticipantesDez()],
    name='Participantes 2016',
    marker_color='lightsalmon'
))

fig.add_trace(go.Bar(
    x=meses,
    y=[ds2017.totalParticipantesJan(), ds2017.totalParticipantesFev(), ds2017.totalParticipantesMar(),
       ds2017.totalParticipantesAbr(), ds2017.totalParticipantesMai(), ds2017.totalParticipantesJun(),
       ds2017.totalParticipantesJul(), ds2017.totalParticipantesAgo(), ds2017.totalParticipantesSet(),
       ds2017.totalParticipantesOut(), ds2017.totalParticipantesNov(), ds2017.totalParticipantesDez()],
    name='Participantes 2017',
    marker_color='blue'
))

fig.add_trace(go.Bar(
    x=meses,
    y=[ds2018.totalParticipantesJan(), ds2018.totalParticipantesFev(), ds2018.totalParticipantesMar(),
       ds2018.totalParticipantesAbr(), ds2018.totalParticipantesMai(), ds2018.totalParticipantesJun(),
       ds2018.totalParticipantesJul(), ds2018.totalParticipantesAgo(), ds2018.totalParticipantesSet(),
       ds2018.totalParticipantesOut(), ds2018.totalParticipantesNov(), ds2018.totalParticipantesDez()],
    name='Participantes 2018',
    marker_color='grey'
))

# Here we modify the tickangle of the xaxis, resulting in rotated labels.
fig.update_layout(barmode='group', xaxis_tickangle=-45, title_text = "Painel de Participantes")
fig.show()