class Punto:

    def __init__(self, x=0, y=0, grado_pertenencia=[], distancias=[]):
        self.x = x
        self.y = y
        self.grado_pertenencia = grado_pertenencia
        self.distancias = distancias

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_grado_pertenencia(self):
        return self.grado_pertenencia

    def get_distancias(self):
        return self.distancias

    def __str__(self):
        return '[' + str(self.x) + ',' + str(self.y) + ']'
