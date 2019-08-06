#### Utilizando a class DOG  #####
import ClassPython

cachorro = ClassPython.Dog("Samuel",26)
print("O nome do meu cachorro é: " + cachorro.nome + " " + "e sua idade é: " + str(cachorro.idade))
cachorro.rolar()
cachorro.sentar()

restaurante = ClassPython.Restaurante("MC Donald","fast-food")
print(restaurante.nome + " " + restaurante.tipo)

restaurante.descricaoRestaurante()
restaurante.restauranteAberto()