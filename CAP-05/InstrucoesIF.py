# Um exemplo simples
carros = ['audi','bmw','subaro','toyota']
for carro in carros:
    if carro == 'bmw':
        print(carro.upper())
    else:
        print(carro.title())
###########################################################
print("####################################################")
for carro in carros:
    if carro != 'bmw':
        print(carro.upper())
    else:
        print(carro)

###########################################################
#Comparações numéricas
#==, !=, <=, >=, <, >

#alem desses operadores de comparação, podemos utilizar o AND e o OR

PAR = 6
IMPAR = 9
if PAR >= 6 or IMPAR <= 9:
    print("sucesso")
else:
    print("insucesso")

#OBS.: O USO DOS PARÊNTESES SÃO OPCIONAIS
if (PAR >= 6) and (IMPAR <= 9):
    print("sucesso")
else:
    print("insucesso")

############################################################## VERIFICANDO SE EXISTE UM ELEMENTO NA LISTA PALAVRA RESERVADA (IN)
print("##############################################################")
# Verificando se um valor está em uma lista
linguagens = ['ingles','portugues','alemao','frances']
print('alemao' in linguagens)

# Verificando se um valor não está em uma lista
if 'mandarim' not in linguagens:
    print("Não consta esse idioma")
else:
    print("Idioma encontrado")



#SINTAXE IF-ELIF-ELSE
media = 7
nota = 6.5

if nota >= media:
    print("aluno aprovado")
elif nota > 3 and nota < media:
    print("aluno em recuperação")
else:
    print("reprovado")


#cores
cor = ['verde','amarelo','vermelho']
homem = 'verde'
if homem == 'azul':
    print("homem é azul")
elif homem == 'amarelo' or homem == 'roxo':
    print("homem amarelo ou roxo")
elif homem == 'verde':
    print("homem verde")

if homem not in cor:
    print("a cor do homem não esta na lista cor")
elif homem in cor:
    print("a cor do homem esta em COR")

#########################################################33
#obs.: UMA LISTA VAZIA É AVALIADA COM FALSE E SE TIVER PELO MENOS UM ELEMENTO É AVALIADA COMO TRUE
frutosDoMar = []
if frutosDoMar:
    print(True)
else:
    print(False)

#verificando se na lista de ingredientes disponiveis contem os ingredientes solicitados
ingredientesDisponivel = ['queijo','tomate','calabresa','cebola','pimentao','azeitona']
ingredientesDesejaveis = ['calabresa','tomate','cebola','batata']

for desejavel in ingredientesDesejaveis:
    if desejavel in ingredientesDisponivel:
        print("adicionado: " + desejavel)
    else:
        print("não temos esse ingrediente: " + desejavel)


#############################################################################
print("#############################################################################")
usuarios = ['admin','colaborador','orelha seca']
usuario = 'admin'
if usuario in usuarios:
    print("Olá "+usuario)
else:
    print("ureia seca")

#### Numeros ordinais
numerosOrdinais = range(1,10)
for numero in numerosOrdinais:
    if numero == 1:
        print(str(numero) + "st")
    elif numero == 2:
        print(str(numero) + "nd")
    elif numero == 3:
        print(str(numero) + "rd")
    elif numero >= 4:
        print(str(numero) + "th")
































































