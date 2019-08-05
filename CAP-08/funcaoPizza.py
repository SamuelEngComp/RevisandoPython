##### ESSA FUNÇÃO SERÁ IMPORTADA POR OUTRO ARQUIVO - FUNCOES.PY


def pizza(tamanho, *ingredientes):
    pizzaCompleta = []
    print("Tamanho da PIZZA: " + str(tamanho))
    for ingrediente in ingredientes:
        pizzaCompleta.append(ingrediente)

    return pizzaCompleta


def pizza2():
    mensagem = "teste de funcao"
    return mensagem

##############################################################33


print(pizza(23,"teste01","teste02","teste03"))