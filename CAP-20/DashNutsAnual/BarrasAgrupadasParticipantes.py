import numpy as np
import matplotlib.pyplot as plt

import DashNuts2015.DashNuts2015 as ds2015
import DashNuts2016.DashNuts2016 as ds2016
import DashNuts2017.DashNuts2017 as ds2017
import DashNuts2018.DashNuts2018 as ds2018

N = 12
atividades2015 = (ds2015.totalParticipantesJan(), ds2015.totalParticipantesFev(), ds2015.totalParticipantesMar(),
                  ds2015.totalParticipantesAbr(), ds2015.totalParticipantesMai(), ds2015.totalParticipantesJun(),
                  ds2015.totalParticipantesJul(), ds2015.totalParticipantesAgo(), ds2015.totalParticipantesSet(),
                  ds2015.totalParticipantesOut(), ds2015.totalParticipantesNov(), ds2015.totalParticipantesDez())

atividades2016 = (ds2016.totalParticipantesJan(), ds2016.totalParticipantesFev(), ds2016.totalParticipantesMar(),
                  ds2016.totalParticipantesAbr(), ds2016.totalParticipantesMai(), ds2016.totalParticipantesJun(),
                  ds2016.totalParticipantesJul(), ds2016.totalParticipantesAgo(), ds2016.totalParticipantesSet(),
                  ds2016.totalParticipantesOut(), ds2016.totalParticipantesNov(), ds2016.totalParticipantesDez())

atividades2017 = (ds2017.totalParticipantesJan(), ds2017.totalParticipantesFev(), ds2017.totalParticipantesMar(),
                  ds2017.totalParticipantesAbr(), ds2017.totalParticipantesMai(), ds2017.totalParticipantesJun(),
                  ds2017.totalParticipantesJul(), ds2017.totalParticipantesAgo(), ds2017.totalParticipantesSet(),
                  ds2017.totalParticipantesOut(), ds2017.totalParticipantesNov(), ds2017.totalParticipantesDez())

atividades2018 = (ds2018.totalParticipantesJan(), ds2018.totalParticipantesFev(), ds2018.totalParticipantesMar(),
                  ds2018.totalParticipantesAbr(), ds2018.totalParticipantesMai(), ds2018.totalParticipantesJun(),
                  ds2018.totalParticipantesJul(), ds2018.totalParticipantesAgo(), ds2018.totalParticipantesSet(),
                  ds2018.totalParticipantesOut(), ds2018.totalParticipantesNov(), ds2018.totalParticipantesDez())


fig, ax = plt.subplots()

ind = np.arange(N)    # the x locations for the groups
width = 0.21         # the width of the bars
p1 = ax.bar(ind - 0.25, atividades2015, width, align='center')
p2 = ax.bar(ind - 0.25 + width, atividades2016, width, align='center')
p3 = ax.bar(ind - 0.25 + width + width, atividades2017, width, align='center')
p4 = ax.bar(ind - 0.25 + width + width + width, atividades2018, width, align='center')

ax.set_title('Participantes 2015 - 2018', fontsize = 20)
ax.set_xticks(ind + width/2)
ax.set_xticklabels(('JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO',
                    'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO'))

ax.legend((p1[0], p2[0], p3[0], p4[0]), ('2015', '2016', '2017', '2018'))
ax.autoscale_view()

plt.show()