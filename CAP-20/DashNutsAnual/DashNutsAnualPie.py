import plotly.graph_objects as go
from plotly.subplots import make_subplots

from ReceberArquivo import ReceberArquivoCSV

import DashNuts2015.DashNuts2015 as ds2015
import DashNuts2016.DashNuts2016 as ds2016
import DashNuts2017.DashNuts2017 as ds2017
import DashNuts2018.DashNuts2018 as ds2018

labels = ["Bancas", "Videoaulas", "Sessão Clinia", "SIG", "EBSERH"]

# Create subplots: use 'domain' type for Pie subplot
#
fig = make_subplots(rows=2, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}],
                                           [{'type':'domain'}, {'type':'domain'}]])
fig.add_trace(go.Pie(labels=labels, values=[ds2015.somaBancas(), ds2015.somaVideoAulas(),
                                            ds2015.somaSessoesClinicas(), ds2015.somaSigs(),
                                            ds2015.somaVCEbserh()], name="Atividades 2015"),
              1, 1)
fig.add_trace(go.Pie(labels=labels, values=[ds2016.somaBancas(), ds2016.somaVideoAulas(),
                                            ds2016.somaSessoesClinicas(), ds2016.somaSigs(),
                                            ds2016.somaVCEbserh()], name="Atividades 2016"),
              1, 2)

fig.add_trace(go.Pie(labels=labels, values=[ds2017.somaBancas(), ds2017.somaVideoAulas(),
                                            ds2017.somaSessoesClinicas(), ds2017.somaSigs(),
                                            ds2017.somaVCEbserh()], name="Atividades 2017"),
              2, 1)

fig.add_trace(go.Pie(labels=labels, values=[ds2018.somaBancas(), ds2018.somaVideoAulas(),
                                            ds2018.somaSessoesClinicas(), ds2018.somaSigs(),
                                            ds2018.somaVCEbserh()], name="Atividades 2018"),
              2, 2)

# Use `hole` to create a donut-like pie chart
fig.update_traces(hole=.4, hoverinfo="label+percent+name")

fig.update_layout(
    title_text="Atividades Nuts 2015 - 2018",
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='2015', x=0.20, y=0.83, font_size=20, showarrow=False),
                 dict(text='2016', x=0.80, y=0.83, font_size=20, showarrow=False),
                 dict(text='2017', x=0.20, y=0.2, font_size=20, showarrow=False),
                 dict(text='2018', x=0.80, y=0.2, font_size=20, showarrow=False)])
fig.show()