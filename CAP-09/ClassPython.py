#### Criando e usando uma classe ###
### Criando e usando uma classe ###
#######################################################################
class Dog():

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def sentar(self):
        print(self.nome.title() + " ------- ")

    def rolar(self):
        print(self.nome.title() + " ------- ")

#######################################################################
class Restaurante():
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def descricaoRestaurante(self):
        print("Nome do restaurante: " + self.nome + " e o tipo é: " + self.tipo)

    def restauranteAberto(self):
        print("O restaurante " + self.nome + " está aberto ")
#######################################################################