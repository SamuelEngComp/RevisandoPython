"""
################################################################################################################
################################################################################################################
########################## MONITORANDO TEMPO, AGENDANDO TAREFAS E INICIANDO PROGRAMAS ##########################
################################################################################################################
################################################################################################################
"""
#MODULO TIME
# Função time.time()

import time

# qtdDeSegundoDesde1970 = time.time()
# print(qtdDeSegundoDesde1970)

## quantos segundo demora um simples laço FOR
# inicio = time.time()
# for i in range(1,100000,1):
#     print(i)
# fim = time.time()
#
# print("Tempo percorrido: ", fim-inicio) ## 11 segundos

## Função time.sleep() --->>> Dentro do Sleep(quantidade de segundos)

# for j in range(1,11,1):
#     time.sleep(2)
#     print(j , " --- ")

# Arredondando números
"""
Basta passar o número que você quer arredondar, além de um
segundo argumento opcional que representa para quantos dígitos após o ponto
decimal você quer arredondar. Se o segundo argumento for omitido, round()
arredondará seu número para o inteiro mais próximo

"""
#
# segundosAgora = time.time()
# print(segundosAgora) # 1566496099.4395492
#
# segundosAgoraArredondadoComDuasCasasDecimais = round(segundosAgora, 2)
# print(segundosAgoraArredondadoComDuasCasasDecimais) # 1566496099.43
#
# segundoArredondadoSemCasasDecimais = round(segundosAgora)
# print(segundoArredondadoSemCasasDecimais) # 1566496099

###############################################################
####################  Projeto: Supercronômetro ################
###############################################################

# Passo 1: Preparar o programa para monitorar tempos

#exibe as introções do programa

# print("ENTER para inicio, ENTER para CLICK e CTRL C para QUIT")
# input()
# print("Iniciando")
# iniciaTime = time.time()
# fimTime = iniciaTime
# numeroDeRodada = 1

# começa a monitorar a duração das rodadas

# Passo 2: Monitorar e exibir os tempos de duração das rodadas

# try:
#     while True:
#         input()
#         rodadaTime = round(time.time()-fimTime, 2)
#         totalTime = round(time.time() - iniciaTime, 2)
#         print('Rodada #%s: %s (%s)' % (numeroDeRodada, totalTime, rodadaTime), end='')
#         numeroDeRodada += 1
#         fimTime = time.time() #reinicia a ultima rodada
# except KeyboardInterrupt: ### quando o usuario prescionar CTRL C ele trata
#     print("\n certo")


#################################################################################
################################ Módulo datetime ################################

import datetime

dataAgora = datetime.datetime.now()
print(dataAgora)
print(dataAgora.day)
print(dataAgora.month)
print(dataAgora.year)
print(dataAgora.hour)
print(dataAgora.minute)
print(dataAgora.second)

nome = input("Digite seu nome: ")
if nome == "samuel":
    print(dataAgora.day,"/",dataAgora.month,"/",dataAgora.year, "------", dataAgora.hour,":",dataAgora.minute,
          ":",dataAgora.second)

#convertendo um tempo especifico
conversao = datetime.datetime.fromtimestamp(1000000)  ## passando um milhão de segundos
print(conversao) ## 1970-01-12 11:46:40

conversao02 = datetime.datetime.fromtimestamp(time.time())
print(conversao02) #2019-08-22 15:47:00.892290

dataDeNascimento = datetime.datetime(1992,12,24,0,0,0)
dataDeHoje = datetime.datetime(2019,8,22,0,0,0)
minhaIdadeHoje = dataDeHoje - dataDeNascimento
print(minhaIdadeHoje)

anos = minhaIdadeHoje.days/365
print(anos)



################################################
###########  Tipo de dado timedelta  ###########
################################################
"""
O módulo datetime também disponibiliza um tipo de dado timedelta que
representa uma duração, em vez de um instante no tempo
"""



































































































