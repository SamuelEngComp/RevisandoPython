import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

import plotly.express as px
import pandas as pd
import plotly.io as entrada

import plotly.graph_objects as go


import DashJaneiro as dj

faixaEtaria = ['Sessão Clínica','Gravação VideoAula','SIG','VC-EBSERH','BANCAS']
quantidadePorFaixaEtaria = [34,56,22,56,65]
# plt.title('Teste de gráfico - faixa etária')
# plt.ylabel('Qtd')
# plt.xlabel('faixa etária')
# plt.bar(faixaEtaria,quantidadePorFaixaEtaria,width=0.33)
# plt.show()

### VERIFICAR OS FAVORITOS DO MOZILA FIREFOX ###
### LÁ TEM UMA PÁGINA COM DICAS PARA A CONSTRUÇÃO DE UM GRÁFICO DE BARRAS BACANA ###

df = pd.DataFrame(dict(r = quantidadePorFaixaEtaria, theta = faixaEtaria))
fig1 = px.line_polar(df, r='r',theta='theta', line_close=True,
                    color_discrete_sequence=px.colors.sequential.Plasma[-7::16])
fig1.show()

def exibirGraficoCopiado():
    categories = ['processing cost', 'mechanical properties', 'chemical stability',
                  'thermal stability', 'device integration']
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[8, 6, 5, 3, 4],
        theta=categories,
        fill='toself',  # tonext
        name='Atividades 2017'
    ))

    fig.add_trace(go.Scatterpolar(
        r=[1, 5, 2, 2, 3],
        theta=categories,
        fill='toself',
        name='Atividades 2018'
    ))
    fig.add_trace(go.Scatterpolar(
        r=[4, 3, 2.5, 1, 2],
        theta=categories,
        fill='toself', #tonext
        name='Atividades 2019'
    ))



    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5]
            )),
        showlegend=True
    )
    fig.show()


