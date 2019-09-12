# mensagem = "mensagem armazenada"
#
# print (mensagem)
#
# mensagem = "Mensagem Alterada"
#
# print (mensagem)
#
# mensagem = "Essa mensagem ja 'foi alterada' muitas vezes"
#
# print (mensagem)
#
# #agora vou utilizar funções da String
mensagemNova = "samuel lima de farias"

# so funcionou pq a versão foi alterada pra 3.7
print(mensagemNova.title())
print(mensagemNova.lower())
print(mensagemNova.upper())

#####################################################################################33

# AGORA VAMOS CONCATENAR STRING
primeiro_nome = "  samuel  "
ultimo_nome = "  farias  "
#
# print(primeiro_nome + " " + ultimo_nome)
# print(primeiro_nome.title() + " " + ultimo_nome.title())

# Acrescentando espaços em branco em strings com tabulações ou quebras de linha

# tabulação
print("Teste de tabulação\t"+"\t"+primeiro_nome+"\t")
# quebra de linha
print("Teste\n de\n quebra\n de\n linha\n")
#espaço em branco
print("Nomes COM espaços-"+primeiro_nome+ultimo_nome)
print("Nomes SEM espaços-"+primeiro_nome.rstrip()+ultimo_nome.rstrip()) #removendo espaço da direita
print("Nomes SEM espaços-"+primeiro_nome.lstrip()+ultimo_nome.lstrip()) #removendo espaço da esquerda
print("Nomes SEM espaços-"+primeiro_nome.strip()+ultimo_nome.strip()) #removendo espaços




















