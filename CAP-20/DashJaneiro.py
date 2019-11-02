
#pegando cada coluna
dados = open("abril2018.csv").readlines()

#colunas da tabela
data = []
atividade = []
tipo = []
participantes = []
tema = []
tempo = []

#atribuindo os dados
for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(",")
        data.append(linha[0])
        atividade.append(linha[1])
        tipo.append(linha[2])
        participantes.append(linha[3])
        tema.append(linha[4])
        tempo.append(linha[5])


#total de atividades no mês
def totalAtividades():
    return int(len(atividade))

#pegando o total de VIDEOCONFERÊNCIA EBSERH no mês
def totalVideoConferenciaEBSERH():
    totalVideoEbserh = (tipo.count("VIDEOCONFERÊNCIA EBSERH") or tipo.count("VIDEOCONFERENCIA EBSERH") or
                            tipo.count("VíDEOCONFERÊNCIA EBSERH"))
    return totalVideoEbserh


#pegando o total de SIG no mês
def totalDeSIGs():
    totalDeSig = tipo.count('SIG')
    return totalDeSig

#pegando o total de VIDEOAULA no mês
def totalDeVideoAulas():
    totalDeVideoAula = (tipo.count('GRAVAÇÃO VIDEOAULA') or
                            tipo.count('GRAVAÇÃO VÍDEOAULA') or
                            tipo.count('GRAVAÇÃO VÍDEO AULA'))
    return totalDeVideoAula

#pegando o total de BANCAS no mês
def totalDeBancas():
    totalBancasTCC = tipo.count('BANCA TCC')
    totalBancasMestrado = tipo.count('BANCA MESTRADO')
    totalBancasDoutorado = tipo.count('BANCA DOUTORADO')
    totalDeBanca = totalBancasTCC+totalBancasMestrado+totalBancasDoutorado
    return totalDeBanca


#pegando o total de SESSÃO no mês
def totalDeSessao():
    totalDeSessao = (tipo.count('SESSÃO') or tipo.count('SESSÃO CLÍNICA') or tipo.count('SESSÃO CLINICA'))
    return totalDeSessao

#pegando o total de participantes no mês
def totalParticipantes():
    totalDeParticipantesJaneiro = 0
    for i in range(0,len(participantes)):
        totalDeParticipantesJaneiro += int(participantes[i])

    return totalDeParticipantesJaneiro


#pegando o total de tempo no mês
def totalTempoMes():
    totalDeTempoEmJaneiro = 0
    for i in range(0, len(tempo)):
        totalDeTempoEmJaneiro += int(tempo[i])

    return totalDeTempoEmJaneiro


#convertendo o tempo de minutos em horas
def conversaoTempo(tempoTotalEmMinutos):
    tempoEmHoras = tempoTotalEmMinutos/60
    return round(tempoEmHoras,2)


#PEGANDO SÓ OS PARTICIPATES DAS SESSÕES:
def participantesApenasDasSessoes():
    qtdParticipantes = 0
    for i in range(len(tipo)):
        if tipo[i] == 'SESSÃO':
            qtdParticipantes += int(participantes[i])

    return qtdParticipantes


#PEGANDO SÓ OS PARTICIPATES DAS VIDEO EBSERH:
def participantesApenasDasVideoEbserh():
    qtdParticipantes = 0
    for i in range(len(tipo)):
         if (tipo[i] == 'VIDEOCONFERÊNCIA EBSERH' or
              tipo[i] == 'VIDEOCONFERENCIA EBSERH' or
              tipo[i] == 'VÍDEOCONFERÊNCIA EBSERH'):
              qtdParticipantes += int(participantes[i])

    return qtdParticipantes


#PEGANDO SÓ OS PARTICIPATES DAS VIDEOAULA:
def participantesApenasDasVideoAulas():
    qtdParticipantes = 0
    for i in range(len(tipo)):
        if tipo[i] == 'GRAVAÇÃO VIDEOAULA' or tipo[i] == 'GRAVAÇÃO VÍDEOAULA':
            qtdParticipantes += int(participantes[i])

    return qtdParticipantes


#PEGANDO SÓ OS PARTICIPATES DOS SIG:
def participantesApenasDoSIG():
    qtdParticipantes = 0
    for i in range(len(tipo)):
        if tipo[i] == 'SIG':
           qtdParticipantes += int(participantes[i])

    return qtdParticipantes

#PEGANDO SÓ OS PARTICIPATES DAS WEB:
def participantesApenasDaWEB():
    qtdParticipantes = 0
    for i in range(len(tipo)):
        if tipo[i] == 'WEBCONFERÊNCIA':
           qtdParticipantes += int(participantes[i])

    return qtdParticipantes

#PEGANDO SÓ OS PARTICIPATES DAS ReuniõesInternas:
def participantesApenasDaReuniaoInterna():
    qtdParticipantes = 0
    for i in range(len(tipo)):
        if tipo[i] == 'REUNIÃO DRª SUZY':
            qtdParticipantes += int(participantes[i])

    return qtdParticipantes

#PEGANDO SÓ OS PARTICIPATES DAS BANCAS:
def participantesApenasDasBancas():
        qtdTCC = 0
        qtdMestrado = 0
        qtdDoutorado = 0
        for i in range(len(tipo)):
            if tipo[i] == 'BANCA TCC':
                qtdTCC += int(participantes[i])

            if tipo[i] == 'BANCA MESTRADO' or tipo[i] == 'BANCA DE MESTRADO':
                qtdMestrado += int(participantes[i])

            if tipo[i] == 'BANCA DOUTORADO' or tipo[i] == 'BANCA DE DOUTORADO':
                qtdDoutorado += int(participantes[i])

        qtdParticipantes = qtdTCC+qtdMestrado+qtdDoutorado
        return qtdParticipantes


#### falta capturar os dados do tempo de cada sessão ####
#PEGANDO SÓ O TEMPO DAS SESSÕES:
def tempoDasSessoes():
    tempoSessao = 0
    for i in range(len(tipo)):
        if tipo[i] == 'SESSÃO':
           tempoSessao += int(tempo[i])

    tempoEmHoras = conversaoTempo(tempoSessao)


    return tempoEmHoras

#PEGANDO SÓ O TEMPO DO SIG:
def tempoDoSIG():
    tempoSig = 0
    for i in range(len(tipo)):
        if tipo[i] == 'SIG':
           tempoSig += int(tempo[i])

    tempoEmHoras = conversaoTempo(tempoSig)

    return tempoEmHoras


#PEGANDO SÓ O TEMPO DAS VIDEOAULAS:
def tempoVideoAulas():
    tempoVideoAula = 0
    for i in range(len(tipo)):
        if tipo[i] == 'GRAVAÇÃO VIDEOAULA' or tipo[i] == 'GRAVAÇÃO VÍDEOAULA':
            tempoVideoAula += int(tempo[i])

    tempoEmHoras = conversaoTempo(tempoVideoAula)


    return tempoEmHoras


#PEGANDO SÓ O TEMPO DAS VIDEO EBSERH:
def tempoVideoEbserh():
    tempoEbserh = 0
    for i in range(len(tipo)):
        if (tipo[i] == 'VIDEOCONFERÊNCIA EBSERH' or
            tipo[i] == 'VIDEOCONFERENCIA EBSERH' or
            tipo[i] == 'VÍDEOCONFERENCIA EBSERH'):
            tempoEbserh += int(tempo[i])

    tempoEmHoras = conversaoTempo(tempoEbserh)


    return tempoEmHoras


def tempoBancas():
    tempoBanca = 0
    for i in range(len(tipo)):
        if (tipo[i] == 'BANCA TCC' or tipo[i] == 'BANCA DE TCC' or
              tipo[i] == 'BANCA MESTRADO' or tipo[i] == 'BANCA DE MESTRADO' or
              tipo[i] == 'BANCA DOUTORADO' or tipo[i] == 'BANCA DE DOUTORADO' or
              tipo[i] == 'BANCA DE QUALIFICAÇÃO DE MESTRADO' or
              tipo[i] == 'BANCA DE QUALIFICAÇÃO DE DOUTORADO' or
              tipo[i] == 'BANCA DE DISSERTAÇÃO DE MESTRADO' or
              tipo[i] == 'BANCA DE DISSERTAÇÃO DE DOUTORADO'):
                tempoBanca += int(tempo[i])

    tempoEmHoras = conversaoTempo(tempoBanca)

    return tempoEmHoras


################## EXIBINDO OS VALORES EXTRAIDOS DA PLANILHA - MÊS - JANEIRO 2018 #####################

def exibirValores():
    print("### EXIBINDO OS VALORES EXTRAIDOS DA PLANILHA - ")
    print("### MÊS - JANEIRO 2018 ######")
    print("################################################")
    print("### QUANTIDADE DE ATIVIDADES")
    print("qtd-atividade - Janeiro: ", totalAtividades())

    print("### QUANTIDADE DE CADA TIPO DE ATIVIDADE")
    print("Total de SESSÃO:", totalDeSessao())
    print("Total de SIG's:", totalDeSIGs())
    print("Total de VIDEOAULAS:", totalDeVideoAulas())
    print("Total VIDEOCONFERENCIA EBSERH:", totalVideoConferenciaEBSERH())
    print("Total BANCAS:", totalDeBancas())

    print("### QUANTIDADE DE PARTICIPANTES")
    print("qtd-participantes no mês: ", totalParticipantes())
    print("qtd-participantes-Sessões: ", participantesApenasDasSessoes())  # BATEU CERTO
    print("qtd-participantes-VideoAulas: ", participantesApenasDasVideoAulas())  # BATEU CERTO
    print("qtd-participantes-SIG: ", participantesApenasDoSIG())  # BATEU CERTO
    print("qtd-participantes-WEB: ", participantesApenasDaWEB())  # BATEU CERTO
    print("qtd-participantes-ReuniãoInterna: ", participantesApenasDaReuniaoInterna())  # BATEU CERTO
    print("qtd-participantes-VIDEOCONFERÊNCIA EBSERH: ", participantesApenasDasVideoEbserh())# BATEU CERTO
    print("qtd-participantes-BANCAS: ", participantesApenasDasBancas())

    print("### TEMPO TOTAL E DE CADA ATIVIDADE")
    print("Total de tempo em Horas em Janeiro: ", conversaoTempo(totalTempoMes()), "h")
    print("Total de Horas de todas Sessões", tempoDasSessoes(), "h")
    print("Total de Horas de todos SIG", tempoDoSIG(), "h")
    print("Total de Horas de todas VideoAulas", tempoVideoAulas(), "h")
    print("Total de Horas de todas VideoConferência Ebserh", tempoVideoEbserh(), "h")
    print("Total de Horas de todas Bancas", tempoBancas(), "h")

    print("#############################################")


print(exibirValores())