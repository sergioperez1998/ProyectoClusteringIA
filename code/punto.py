import collections


class Punto(collections.namedtuple('_Punto', 'x y')):

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    # def getCoordenadas(self):
    #     return '[' + str(self.x) + ',' + str(self.y) + ']'

    def __str__(self):
        return '[' + str(self.x) + ',' + str(self.y) + ']'
