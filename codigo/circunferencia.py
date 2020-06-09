class Circunferencia:

    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio
        self.lista_puntos = []

    def get_centro(self):
        return self.centro

    def get_radio(self):
        return self.radio

    def get_lista_puntos(self):
        return self.lista_puntos

    def __str__(self):
        msg = "Centro: {0}, Radio: {1}, Lista de puntos: {2}"
        return msg.format(self.centro, self.radio, self.lista_puntos)
