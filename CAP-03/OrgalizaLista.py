#ORGANIZANDO LISTA


funcionarios = ['joão','Maria',"jose",'Neymar']

# Ordenando uma lista de forma permanente com o método sort()
funcionarios.sort()
print(funcionarios)

funcionarios.sort(reverse=True)
print(funcionarios)

# Ordenando uma lista temporariamente com a função sorted()
print(funcionarios)
print(sorted(funcionarios))

# Exibindo uma lista em ordem inversa
print(funcionarios)
funcionarios.reverse()
print(funcionarios)
funcionarios.reverse()
print(funcionarios)

# Descobrindo o tamanho de uma lista
tamanhoLista = len(funcionarios)
print(tamanhoLista)
nova = []
for i in range(tamanhoLista):
    teste = funcionarios[i].upper()
    print(teste)
    nova.append(teste)


print(nova)


# Evitando erros de índice quando trabalhar com listas
# OBS.: PARA EVITAR ACESSAR O ULTIMO ELEMENTO DE UMA LISTA E DAR UM ERRO, FAZEMOS O SEGUINTE, ACESSAMOS UTILIZANDO O -1
# ASSIM COM O -1, SEMPRE RETORNA O ULTIMO ELEMENTO


## STOP CAP-04 TRABALHANDO COM LISTAS
