import collections


class Punto(collections.namedtuple('_Punto', 'x y')):

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getCoordenadas(self):
        return '[' + self.x + ',' + self.y + ']'

    def __str__(self):
        msg = "Punto con coordenadas {0} en x, {1} en y"
        return msg.format(self.x, self.y)
