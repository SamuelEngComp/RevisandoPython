# Módulo datetime

from datetime import datetime, timezone #modulo datetime tem uma class datetime que tem um metodo strptime
from matplotlib import pyplot as p
import json
import pygal
from pygal_maps_world.maps import World ### maneira certa do mapaMundi


# dataParaColocarNoPadrao = datetime.strptime('2019-08-10','%Y-%m-%d')
# print(dataParaColocarNoPadrao)
#
# dataAgora = datetime.now(timezone.utc)
# print(dataAgora)
#
# # Plotando datas
# figura = p.figure(dpi=128, figsize=(10,6))
# p.plot(dataParaColocarNoPadrao,c ='red')
# figura.autofmt_xdate()
# p.show()

## DEVIDO PROBLEMAS NO DOWNLOAD DO ARQUIVO DE DADOS, NÃO CONSEGUI FAZER OS GRÁFICOS, LOGO ESSE MODULO DE ARQUIVO 'CSV'
## E PLOTAGEM VOU FAZER PELA INTERNET, VISUALIZANDO A DOCUMENTAÇÃO
## - PLOTANDO DADOS DO CSV;
## - PLOTANDO DATAS;
## - PLOTANDO PERIODOS;
## - ESTILIZANDO OS GRÁFICOS;
## - VERIFICAR OS ERROS QUANDO A LEITURA DE CSV FALHAR
## - OUTRA COISA QUE PRECISO ESTUDAR E VERIFCAR COMO UTILIZAR NO PYCHAR: Mapeando conjuntos de dados globais: formato JSON
## - IMPORT JSON - PRECISA SER ESTUDADA
## - COMO CONSTRUIR UM MAPA MUNDI COM A BIBLIOTECA PYGAL

# Convertendo strings em valores numéricos
# PARA ISSO BASTA UTILIZAR A FUNÇÃO INT()
# EX.:
#
# chaveValor = {
#     "nome":"samuel",
#     "idade":"23"
# }
#
# for key, value in chaveValor.items():
#     print(value)
#
#     if value == "23":
#         valorConvertido = int(value)
#         print(valorConvertido)
#         valorConvertido += 1
#         print(valorConvertido)


# mapaMundi = World()
# mapaMundi.title = 'Norte, Central e Sul'
# mapaMundi.add('Norte',['ca','mx','us'])
# mapaMundi.add('Central',['ma', 'mc', 'md', 'me', 'mg','mk', 'ml', 'mm', 'mn', 'mo','mr', 'mt', 'mu', 'mv', 'mw'])
# mapaMundi.add('Sul',['ar','br','cl'])
# mapaMundi.render_in_browser()

# Plotando dados numéricos em um mapa-múndi

mapaMundi = World()
mapaMundi.title = 'Norte, Central e Sul'
mapaMundi.add('Norte',{'ca':21,'mx':22,'us':23})
mapaMundi.add('Central',{'ma':42, 'mc':33, 'md':421, 'me':45, 'mg':31,'mk':11, 'ml':48, 'mm':44, 'mn':76, 'mo':9})
mapaMundi.add('Sul',{'ar':22,'br':11,'cl':34})
mapaMundi.render_in_browser()