# Gerando exceções
codigo = ''
try:
    codigo
except Exception as erro:
    codigo

###### Asserções ->>>  é uma verificação de sanidade para garantir que seu código não está fazendo nada obviamente incorreto.
# Usando uma asserção em uma simulação de semáforo

semaforo01 = {
    'ns':'verde',
    'lo':'vermelho'
}
semaforo02 = {
    'ns':'vermelho',
    'lo':'verde'
}

# LOGGING
import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.debug("Inicio do programa")
#
# def fatorial(numero):
#     logging.debug("Inicio fatorial (%s%%)"%(numero))
#     total = 1
#     for i in range(1, numero+1):
#         total *= i
#         logging.debug("é " + str(i) + ", total de " + str(total))
#
#     logging.debug("Fim fatorial(%s%%)"%(numero))
#     return total
#
# print(fatorial(5))

## GRAVANDO O LOG EM UM ARQUIVO.TXT
arquivoLog = open("arquivoLog.txt","w")

logging.basicConfig(filename='arquivoLog.txt',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug("Inicio do programa")

def fatorial(numero):
    logging.debug("Inicio fatorial (%s%%)"%(numero))
    total = 1
    for i in range(1, numero+1):
        total *= i
        logging.debug("é " + str(i) + ", total de " + str(total))

    logging.debug("Fim fatorial(%s%%)"%(numero))
    return total

print(fatorial(5))




