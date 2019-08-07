#### Criando e usando uma classe ###
### Criando e usando uma classe ###
#######################################################################

# class Dog():
#
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#
#     def sentar(self):
#         print(self.nome.title() + " ------- ")
#
#     def rolar(self):
#         print(self.nome.title() + " ------- ")

#######################################################################

# class Restaurante():
#     def __init__(self, nome, tipo):
#         self.nome = nome
#         self.tipo = tipo
#
#     def descricaoRestaurante(self):
#         print("Nome do restaurante: " + self.nome + " e o tipo é: " + self.tipo)
#
#     def restauranteAberto(self):
#         print("O restaurante " + self.nome + " está aberto ")
#######################################################################

## HERANÇA ##
class carro(object): ## CLASSE PAI
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def andar(self):
        print("Esse metodo pertence a classe pai")

class carroEletrico(carro):  ## HERANÇA - CLASSE FILHA
    def __init__(self, modelo, ano, rodas):
        # super(carroEletrico,self).__init__(modelo, ano)  ## aqui no metodo INIT não precisa colocar o self
        # para o python 2.7 era necessario inserir a class filha e o self no metodo super(), agora não é mais necessário
        super().__init__(modelo, ano)
        self.rodas = rodas

    def retorneModeloAno(self):
        return self.modelo + " " + self.ano + " " + self.rodas

    def andar(self):
        print("Esse metodo pertence a classe filha")

meuCarro = carroEletrico("celta",1992,4)
print(meuCarro.modelo)
print(meuCarro.ano)
print(str(meuCarro.rodas))

meuCarro.andar() ## SOBRESCREVER UM METODO DA CLASS PAI, BASTA ESCREVER O MESMO METODO NA CLASS FILHA

carroNovo = carro("T-CROSS", 2020)
print(carroNovo.modelo)

# print(meuCarro.modelo + str(meuCarro.ano)) ## UTILIZANDO A HERANÇA

# meuCarro02 = carroEletrico("celta02",1993,4)
# print(meuCarro02.rodas)
#######################################################################

















