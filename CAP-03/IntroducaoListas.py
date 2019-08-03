# Acessando elementos de uma lista
funcionarios = ['joão','Maria',"jose",'Neymar']
print(funcionarios[2])
print(funcionarios[-1]) #acessando sempre o ultimo elemento da lista
print(funcionarios[-2])

# NOMES
funcionarios = ['joão','Maria',"jose",'Neymar']
print(funcionarios[0])
print(funcionarios[1])
print(funcionarios[2])
print(funcionarios[3])

#SAUDAÇÕES #LISTA
print("Mensagem teste "+funcionarios[0].title()+" Talkey")
print("Mensagem teste "+funcionarios[1].title()+" Talkey")
print("Mensagem teste "+funcionarios[2].title()+" Talkey")
print("Mensagem teste "+funcionarios[3].title()+" Talkey")

# Alterando, acrescentando e removendo elementos
#Modificando elementos de uma lista
novaLista = ['dell','hp','positivo','intelbras']
print(novaLista)
novaLista[2] = 'Sansung'
print(novaLista)

# Acrescentando elementos em uma lista
novaLista.insert(4,'IBM')
novaLista.insert(1,'amazon') #adiciono o elemento em qualquer posição da lista
print(novaLista)

novaLista.append('NVIDIA') #FOI ACRESCENTADO NO FINAL DA LISTA
print(novaLista)

# Removendo elementos de uma lista
# Removendo um item usando a instrução del
del novaLista[2]
print(novaLista)

# Removendo um item com o método pop()
novaLista.pop(3) #escolhendo o elemento
print(novaLista)
novaLista.pop() #removendo o topo da pilha ou o fim da fila
print(novaLista)

#OBS.: COM O METODO POP() EU POSSO UTILIZAR O ELEMENTO QUE FOI REMOVIDO, COM O METODO DEL, EU NÃO POSSO UTILIZAR ESSE ELEMENTO

# Removendo um item de acordo com o valor
# REMOVE() e passa o valor... outra coisa é que podemos utilizar o valor removido
novaLista.remove('IBM')
print(novaLista)

#LISTA DE CONVIDADOS
listaConvidados = ['joao', 'maria', 'jose', 'DaniAlves', 'Neymidia', 'Messi', 'CR7']
print('Não poderá comparecer '+ listaConvidados[4])
listaConvidados.pop(4)
listaConvidados.insert(4,'Love')
print(listaConvidados)
listaConvidados.insert(0,'miguel')
listaConvidados.insert(4,'Judas')
listaConvidados.append('junior')
print(listaConvidados)

print("DESCULPE " + listaConvidados.pop())
print(listaConvidados)
print("DESCULPE " + listaConvidados.pop())
print("DESCULPE " + listaConvidados.pop())
print("DESCULPE " + listaConvidados.pop())
print("DESCULPE " + listaConvidados.pop())
print(listaConvidados)
del listaConvidados[0]
print(listaConvidados)
del listaConvidados[0]
del listaConvidados[0]
print(listaConvidados)
del listaConvidados[0]
del listaConvidados[0]
print(listaConvidados)