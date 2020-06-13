class Punto:

    def __init__(self, x=0, y=0, grado_pertenencia=[]):
        self.x = x
        self.y = y
        self.grado_pertenencia = grado_pertenencia

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_grado_pertenencia(self):
        return self.grado_pertenencia

    def __str__(self):
        return '[' + str(self.x) + ',' + str(self.y) + ']'

    def __eq__(self, other):
        if not isinstance(other, Punto):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.get_x() == other.get_x() and self.get_y() == other.get_y()