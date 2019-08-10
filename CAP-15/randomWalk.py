from random import choice

class RandomWalk():
    def __init__(self,numPontos = 5000):
        self.numPontos = numPontos
        self.x = [0]
        self.y = [0]

    def fill_walk(self):
        while len(self.x) < self.numPontos:
            xDirecao = choice([1,-1])
            xDistancia = choice([0,1,2,3,4])
            xPasso = xDirecao * xDistancia

            yDirecao = choice([1, -1])
            yDistancia = choice([0, 1, 2, 3, 4])
            yPasso = yDirecao * yDistancia

            if xPasso == 0 and yPasso == 0:
                continue

            xProximo = self.x[-1] + xPasso
            yProximo = self.y[-1] + yPasso
            self.x.append(xProximo)
            self.y.append(yProximo)