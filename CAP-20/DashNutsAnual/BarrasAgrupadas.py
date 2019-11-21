import numpy as np
import matplotlib.pyplot as plt

import DashNuts2015.DashNuts2015 as ds2015
import DashNuts2016.DashNuts2016 as ds2016
import DashNuts2017.DashNuts2017 as ds2017
import DashNuts2018.DashNuts2018 as ds2018

N = 12
atividades2015 = (ds2015.totalAtivJaneiro(), ds2015.totalAtivFevereiro(), ds2015.totalAtivMarco(),
                  ds2015.totalAtivAbril(), ds2015.totalAtivMaio(), ds2015.totalAtivJunho(),
                  ds2015.totalAtivJulho(), ds2015.totalAtivAgosto(), ds2015.totalAtivSetembro(),
                  ds2015.totalAtivOutubro(), ds2015.totalAtivNovembro(), ds2015.totalAtivDezembro())

atividades2016 = (ds2016.totalAtivJaneiro(), ds2016.totalAtivFevereiro(), ds2016.totalAtivMarco(),
                  ds2016.totalAtivAbril(), ds2016.totalAtivMaio(), ds2016.totalAtivJunho(),
                  ds2016.totalAtivJulho(), ds2016.totalAtivAgosto(), ds2016.totalAtivSetembro(),
                  ds2016.totalAtivOutubro(), ds2016.totalAtivNovembro(), ds2016.totalAtivDezembro())

atividades2017 = (ds2017.totalAtivJaneiro(), ds2017.totalAtivFevereiro(), ds2017.totalAtivMarco(),
                  ds2017.totalAtivAbril(), ds2017.totalAtivMaio(), ds2017.totalAtivJunho(),
                  ds2017.totalAtivJulho(), ds2017.totalAtivAgosto(), ds2017.totalAtivSetembro(),
                  ds2017.totalAtivOutubro(), ds2017.totalAtivNovembro(), ds2017.totalAtivDezembro())

atividades2018 = (ds2018.totalAtivJaneiro(), ds2018.totalAtivFevereiro(), ds2018.totalAtivMarco(),
                  ds2018.totalAtivAbril(), ds2018.totalAtivMaio(), ds2018.totalAtivJunho(),
                  ds2018.totalAtivJulho(), ds2018.totalAtivAgosto(), ds2018.totalAtivSetembro(),
                  ds2018.totalAtivOutubro(), ds2018.totalAtivNovembro(), ds2018.totalAtivDezembro())

mesesDoano = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO',
                    'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']

fig, ax = plt.subplots()

ind = np.arange(N)    # the x locations for the groups
width = 0.21         # the width of the bars
p1 = ax.bar(ind - 0.25, atividades2015, width, align='center')
p2 = ax.bar(ind - 0.25 + width, atividades2016, width, align='center')
p3 = ax.bar(ind - 0.25 + width + width, atividades2017, width, align='center')
p4 = ax.bar(ind - 0.25 + width + width + width, atividades2018, width, align='center')


ax.set_title('ATIVIDADES 2015 - 2018', fontsize = 55)
ax.set_xticks(ind + width/2)
ax.set_xticklabels(('JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO',
                    'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO'))

ax.legend((p1[0], p2[0], p3[0], p4[0]), ('2015', '2016', '2017', '2018'))
ax.autoscale_view()
plt.plot(mesesDoano, atividades2015, color = "red", marker = "x", label = "2015")
plt.plot(mesesDoano, atividades2016, color = "blue", marker = "x", label = "2016")
plt.plot(mesesDoano, atividades2017, color = "orange", marker = "x", label = "2017")
plt.plot(mesesDoano, atividades2018, color = "grey", marker = "x", label = "2018")
plt.show()