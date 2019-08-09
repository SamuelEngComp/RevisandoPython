##TESTANDO O CODIGO - CAP 11
#Testando uma função
import unittest

def nomeCompleto(primeiroNome, segundoNome):
    nomeC = primeiroNome.title() + " " + segundoNome.title()
    return nomeC

print("digite 'q' para sair")
while True:
    nome01 = input("Digite o primeiro nome: ")
    if nome01 == 'q':
        break

    nome02 = input("Digite o segundo nome: ")
    if nome02 == 'q':
        break

    print(nomeCompleto(nome01, nome02))

unittest.main()
# Testes de unidade e casos de teste
# Um teste que passa
##METODO |||||||||||||||||| USO
# assertEqual(a, b) Verifica se a == b
# assertNotEqual(a, b) Verifica se a != b
# assertTrue(x) Verifica se x é True
# assertFalse(x) Verifica se x é False
# assertIn(item, lista) Verifica se item está em lista
# assertNotIn(item, lista) Verifica se item não está em lista

#OBS.: Só pode usar esses métodos somente em uma classe que herde de unittest





