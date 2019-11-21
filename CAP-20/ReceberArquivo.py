## Autor: Samuel Farias
## Ano: 2019
## Descrição: Essa class quando for instanciada é necessário passar o caminho do arquivo csv, não esquecer da extensão .csv
## exemplo: dadosJaneiro = ReceberArquivoCSV("janeiro2018.csv")
class ReceberArquivoCSV():

    ##método init, ele inicia tudo,assim eu consigo instanciar todas as variáveis.
    def __init__(self, nomeDoArquivoCSV):
        self.nomeDoArquivoCSV = nomeDoArquivoCSV
        dados = open(nomeDoArquivoCSV).readlines()
        self.data = []
        self.atividade = []
        self.tipo = []
        self.participantes = []
        self.tema = []
        self.tempo = []

        # atribuindo os dados
        for i in range(len(dados)):
            if i != 0:
                linha = dados[i].split(",")
                self.data.append(linha[0])
                self.atividade.append(linha[1])
                self.tipo.append(linha[2])
                self.participantes.append(linha[3])
                self.tema.append(linha[4])
                self.tempo.append(linha[5])


    # total de atividades no mês
    def totalAtividades(self):
        return int(len(self.atividade))

    # pegando o total de VIDEOCONFERÊNCIA EBSERH no mês
    def totalVideoConferenciaEBSERH(self):
        totalVideoEbserh = (self.tipo.count("VIDEOCONFERÊNCIA EBSERH") or self.tipo.count("VIDEOCONFERENCIA EBSERH") or
                            self.tipo.count("VíDEOCONFERÊNCIA EBSERH"))
        return totalVideoEbserh

    # pegando o total de SIG no mês
    def totalDeSIGs(self):
        totalDeSig = self.tipo.count('SIG')
        return totalDeSig

    # pegando o total de VIDEOAULA no mês
    def totalDeVideoAulas(self):
        totalDeVideoAula = (self.tipo.count('GRAVAÇÃO VIDEOAULA') or
                            self.tipo.count('GRAVAÇÃO VÍDEOAULA') or
                            self.tipo.count('GRAVAÇÃO VÍDEO AULA'))
        return totalDeVideoAula

    # pegando o total de BANCAS no mês
    def totalDeBancas(self):
        totalBancasTCC = self.tipo.count('BANCA TCC')
        totalBancasDeTCC = self.tipo.count('BANCA DE TCC')
        totalBancasMestrado = self.tipo.count('BANCA MESTRADO')
        totalBancasDeMestrado = self.tipo.count('BANCA DE MESTRADO')
        totalBancasDoutorado = self.tipo.count('BANCA DOUTORADO')
        totalBancasDeDoutorado = self.tipo.count('BANCA DE DOUTORADO')
        totalDeBanca = totalBancasDeDoutorado + totalBancasDeMestrado + totalBancasDeTCC + \
                       totalBancasTCC + totalBancasMestrado + totalBancasDoutorado
        return totalDeBanca

    # pegando o total de SESSÃO no mês
    def totalDeSessao(self):
        totalDeSessao = (self.tipo.count('SESSÃO') or self.tipo.count('SESSÃO CLÍNICA') or self.tipo.count('SESSÃO CLINICA'))
        return totalDeSessao

    # pegando o total de participantes no mês
    def totalParticipantes(self):
        totalDeParticipantesJaneiro = 0
        for i in range(0, len(self.participantes)):
            totalDeParticipantesJaneiro += int(self.participantes[i])

        return totalDeParticipantesJaneiro

    # pegando o total de tempo no mês
    def totalTempoMes(self):
        totalDeTempoEmJaneiro = 0
        for i in range(0, len(self.tempo)):
            totalDeTempoEmJaneiro += int(self.tempo[i])

        return totalDeTempoEmJaneiro

    # convertendo o tempo de minutos em horas
    def conversaoTempo(tempoTotalEmMinutos):
        tempoEmHoras = tempoTotalEmMinutos/60
        return round(tempoEmHoras, 2)

    # PEGANDO SÓ OS PARTICIPATES DAS SESSÕES:
    def participantesApenasDasSessoes(self):
        qtdParticipantes = 0
        for i in range(len(self.tipo)):
            if self.tipo[i] == 'SESSÃO':
                qtdParticipantes += int(self.participantes[i])

        return qtdParticipantes

    # PEGANDO SÓ OS PARTICIPATES DAS VIDEO EBSERH:
    def participantesApenasDasVideoEbserh(self):
        qtdParticipantes = 0
        for i in range(len(self.tipo)):
            if (self.tipo[i] == 'VIDEOCONFERÊNCIA EBSERH' or
                    self.tipo[i] == 'VIDEOCONFERENCIA EBSERH' or
                    self.tipo[i] == 'VÍDEOCONFERÊNCIA EBSERH'):
                qtdParticipantes += int(self.participantes[i])

        return qtdParticipantes

    # PEGANDO SÓ OS PARTICIPATES DAS VIDEOAULA:
    def participantesApenasDasVideoAulas(self):
        qtdParticipantes = 0
        for i in range(len(self.tipo)):
            if self.tipo[i] == 'GRAVAÇÃO VIDEOAULA' or self.tipo[i] == 'GRAVAÇÃO VÍDEOAULA':
                qtdParticipantes += int(self.participantes[i])

        return qtdParticipantes

    # PEGANDO SÓ OS PARTICIPATES DOS SIG:
    def participantesApenasDoSIG(self):
        qtdParticipantes = 0
        for i in range(len(self.tipo)):
            if self.tipo[i] == 'SIG':
                qtdParticipantes += int(self.participantes[i])

        return qtdParticipantes

    # PEGANDO SÓ OS PARTICIPATES DAS WEB:
    def participantesApenasDaWEB(self):
        qtdParticipantes = 0
        for i in range(len(self.tipo)):
            if self.tipo[i] == 'WEBCONFERÊNCIA':
                qtdParticipantes += int(self.participantes[i])

        return qtdParticipantes

    # PEGANDO SÓ OS PARTICIPATES DAS ReuniõesInternas:
    def participantesApenasDaReuniaoInterna(self):
        qtdParticipantes = 0
        for i in range(len(self.tipo)):
            if self.tipo[i] == 'REUNIÃO DRª SUZY':
                qtdParticipantes += int(self.participantes[i])

        return qtdParticipantes

    # PEGANDO SÓ OS PARTICIPATES DAS BANCAS:
    def participantesApenasDasBancas(self):
        qtdTCC = 0
        qtdMestrado = 0
        qtdDoutorado = 0
        for i in range(len(self.tipo)):
            if self.tipo[i] == 'BANCA TCC':
                qtdTCC += int(self.participantes[i])

            if self.tipo[i] == 'BANCA MESTRADO' or self.tipo[i] == 'BANCA DE MESTRADO':
                qtdMestrado += int(self.participantes[i])

            if self.tipo[i] == 'BANCA DOUTORADO' or self.tipo[i] == 'BANCA DE DOUTORADO':
                qtdDoutorado += int(self.participantes[i])

        qtdParticipantes = qtdTCC + qtdMestrado + qtdDoutorado
        return qtdParticipantes

    #### falta capturar os dados do tempo de cada sessão ####
    # PEGANDO SÓ O TEMPO DAS SESSÕES:
    def tempoDasSessoes(self):
        tempoSessao = 0
        for i in range(len(self.tipo)):
            if self.tipo[i] == 'SESSÃO':
                tempoSessao += int(self.tempo[i])

        tempoEmHoras = self.conversaoTempo(tempoSessao)

        return tempoEmHoras

    # PEGANDO SÓ O TEMPO DO SIG:
    def tempoDoSIG(self):
        tempoSig = 0
        for i in range(len(self.tipo)):
            if self.tipo[i] == 'SIG':
                tempoSig += int(self.tempo[i])

        tempoEmHoras = self.conversaoTempo(tempoSig)

        return tempoEmHoras

    # PEGANDO SÓ O TEMPO DAS VIDEOAULAS:
    def tempoVideoAulas(self):
        tempoVideoAula = 0
        for i in range(len(self.tipo)):
            if self.tipo[i] == 'GRAVAÇÃO VIDEOAULA' or self.tipo[i] == 'GRAVAÇÃO VÍDEOAULA':
                tempoVideoAula += int(self.tempo[i])

        tempoEmHoras = self.conversaoTempo(tempoVideoAula)

        return tempoEmHoras

    # PEGANDO SÓ O TEMPO DAS VIDEO EBSERH:
    def tempoVideoEbserh(self):
        tempoEbserh = 0
        for i in range(len(self.tipo)):
            if (self.tipo[i] == 'VIDEOCONFERÊNCIA EBSERH' or
                    self.tipo[i] == 'VIDEOCONFERENCIA EBSERH' or
                    self.tipo[i] == 'VÍDEOCONFERENCIA EBSERH'):
                tempoEbserh += int(self.tempo[i])

        tempoEmHoras = self.conversaoTempo(self.tempoEbserh)

        return tempoEmHoras

    def tempoBancas(self):
        tempoBanca = 0
        for i in range(len(self.tipo)):
            if (self.tipo[i] == 'BANCA TCC' or self.tipo[i] == 'BANCA DE TCC' or
                    self.tipo[i] == 'BANCA MESTRADO' or self.tipo[i] == 'BANCA DE MESTRADO' or
                    self.tipo[i] == 'BANCA DOUTORADO' or self.tipo[i] == 'BANCA DE DOUTORADO' or
                    self.tipo[i] == 'BANCA DE QUALIFICAÇÃO DE MESTRADO' or
                    self.tipo[i] == 'BANCA DE QUALIFICAÇÃO DE DOUTORADO' or
                    self.tipo[i] == 'BANCA DE DISSERTAÇÃO DE MESTRADO' or
                    self.tipo[i] == 'BANCA DE DISSERTAÇÃO DE DOUTORADO'):
                tempoBanca += int(self.tempo[i])

        tempoEmHoras = self.conversaoTempo(tempoBanca)

        return tempoEmHoras