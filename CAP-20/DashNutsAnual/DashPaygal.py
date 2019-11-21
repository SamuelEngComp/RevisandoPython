import pygal
import cairosvg

from ReceberArquivo import ReceberArquivoCSV
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np

import DashNuts2015.DashNuts2015 as ds2015
import DashNuts2016.DashNuts2016 as ds2016
import DashNuts2017.DashNuts2017 as ds2017
import DashNuts2018.DashNuts2018 as ds2018

MesesDoAno = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro",
              "Novembro", "Dezembro"]

line_chart = pygal.Bar(width = 1600, heigth = 1000)
line_chart.title = 'Participantes'
line_chart.x_labels = map(str, range(len(MesesDoAno)))
line_chart.add('2015', [ds2015.totalParticipantesJan(), ds2015.totalParticipantesFev(), ds2015.totalParticipantesMar(),
                        ds2015.totalParticipantesAbr(), ds2015.totalParticipantesMai(), ds2015.totalParticipantesJun(),
                        ds2015.totalParticipantesJul(), ds2015.totalParticipantesAgo(), ds2015.totalParticipantesSet(),
                        ds2015.totalParticipantesOut(), ds2015.totalParticipantesNov(), ds2015.totalParticipantesDez()])

line_chart.add('2016', [ds2016.totalParticipantesJan(), ds2016.totalParticipantesFev(), ds2016.totalParticipantesMar(),
                        ds2016.totalParticipantesAbr(), ds2016.totalParticipantesMai(), ds2016.totalParticipantesJun(),
                        ds2016.totalParticipantesJul(), ds2016.totalParticipantesAgo(), ds2016.totalParticipantesSet(),
                        ds2016.totalParticipantesOut(), ds2016.totalParticipantesNov(), ds2016.totalParticipantesDez()])

line_chart.add('2017', [ds2017.totalParticipantesJan(), ds2017.totalParticipantesFev(), ds2017.totalParticipantesMar(),
                        ds2017.totalParticipantesAbr(), ds2017.totalParticipantesMai(), ds2017.totalParticipantesJun(),
                        ds2017.totalParticipantesJul(), ds2017.totalParticipantesAgo(), ds2017.totalParticipantesSet(),
                        ds2017.totalParticipantesOut(), ds2017.totalParticipantesNov(), ds2017.totalParticipantesDez()])

line_chart.add('2018', [ds2018.totalParticipantesJan(), ds2018.totalParticipantesFev(), ds2018.totalParticipantesMar(),
                        ds2018.totalParticipantesAbr(), ds2018.totalParticipantesMai(), ds2018.totalParticipantesJun(),
                        ds2018.totalParticipantesJul(), ds2018.totalParticipantesAgo(), ds2018.totalParticipantesSet(),
                        ds2018.totalParticipantesOut(), ds2018.totalParticipantesNov(), ds2018.totalParticipantesDez()])

line_chart.render_to_png(filename="Bar", dpi= 2000)


import pygal                                                       # First import pygal
bar_chart = pygal.Bar()                                            # Then create a bar graph object
bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])  # Add some values
bar_chart.render_to_png(filename= "BarraTeste2",dpi= 1000)


gauge = pygal.SolidGauge(inner_radius=0.70)
percent_formatter = lambda x: '{:.10g}%'.format(x)
dollar_formatter = lambda x: '{:.10g}$'.format(x)
gauge.value_formatter = percent_formatter

gauge.add('Series 1', [{'value': 225000, 'max_value': 1275000}],
          formatter=dollar_formatter)
gauge.add('Series 2', [{'value': 110, 'max_value': 100}])
gauge.add('Series 3', [{'value': 3}])
gauge.add(
    'Series 4', [
        {'value': 51, 'max_value': 100},
        {'value': 12, 'max_value': 100}])
gauge.add('Series 5', [{'value': 79, 'max_value': 100}])
gauge.add('Series 6', 99)
gauge.add('Series 7', [{'value': 100, 'max_value': 100}])
gauge.render(is_unicode=False)


bar_chart = pygal.HorizontalStackedBar()
bar_chart.title = "Remarquable sequences"
bar_chart.x_labels = map(str, range(11))
bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
bar_chart.add('Padovan', [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12])
bar_chart.render_to_png(filename="BarraHorizontal", dpi=1000)

line_chart = pygal.Line(width = 1000)
line_chart.title = 'Alterei a largura (in %)'
line_chart.x_labels = map(str, range(2002, 2013))
line_chart.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
line_chart.render_to_png(filename="SoLinhas", dpi=1000)


line_chart = pygal.HorizontalBar(width = 1600, height = 800)
line_chart.title = 'Browser usage in February 2012 (in %)'
line_chart.add('IE', 19.5)
line_chart.add('Firefox', 36.6)
line_chart.add('Chrome', 36.3)
line_chart.add('Safari', 4.5)
line_chart.add('Opera', 2.3)
line_chart.render_to_png(filename="SoBarrasH", dpi=1000)

pie_chart = pygal.Pie(inner_radius=.4)
pie_chart.title = 'Browser usage in February 2012 (in %)'
pie_chart.add('IE', 19.5)
pie_chart.add('Firefox', 36.6)
pie_chart.add('Chrome', 36.3)
pie_chart.add('Safari', 4.5)
pie_chart.add('Opera', 2.3)
pie_chart.render_to_png(filename="pizzaCortada", dpi=1000)

radar_chart = pygal.Radar()
radar_chart.title = 'V8 benchmark results'
radar_chart.x_labels = ['Richards', 'DeltaBlue', 'Crypto', 'RayTrace', 'EarleyBoyer', 'RegExp', 'Splay', 'NavierStokes']
radar_chart.add('Chrome', [6395, 8212, 7520, 7218, 12464, 1660, 2123, 8607])
radar_chart.add('Firefox', [7473, 8099, 11700, 2651, 6361, 1044, 3797, 9450])
radar_chart.add('Opera', [3472, 2933, 4203, 5229, 5810, 1828, 9013, 4669])
radar_chart.add('IE', [43, 41, 59, 79, 144, 136, 34, 102])
radar_chart.render_to_png(filename="Radar", dpi=1000)



# gauge = pygal.SolidGauge(
#     half_pie=True, inner_radius=0.70,
#     style=pygal.style.styles['default'](value_font_size=10))
#
# percent_formatter = lambda x: '{:.10g}%'.format(x)
# dollar_formatter = lambda x: '{:.10g}$'.format(x)
# gauge.value_formatter = percent_formatter
#
# gauge.add('Series 1', [{'value': 225000, 'max_value': 1275000}],
#           formatter=dollar_formatter)
# gauge.add('Series 2', [{'value': 110, 'max_value': 100}])
# gauge.add('Series 3', [{'value': 3}])
# gauge.add(
#     'Series 4', [
#         {'value': 51, 'max_value': 100},
#         {'value': 12, 'max_value': 100}])
# gauge.add('Series 5', [{'value': 79, 'max_value': 100}])
# gauge.add('Series 6', 99)
# gauge.add('Series 7', [{'value': 100, 'max_value': 100}])
# gauge.render_to_png(filename="metadePizza", dpi=1000)