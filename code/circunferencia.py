class Circunferencia(object):

    def __init__(self, centro, radio, listaPuntos):
        self.centro = centro
        self.radio = radio
        self.listaPuntos = listaPuntos

    def getCentro(self):
        return self.centro

    def getRadio(self):
        return self.radio

    def getListaPuntos(self):
        return self.listaPuntos

    def __str__(self):
        msg = "Centro: {0}, Radio: {1}, Lista de puntos: {2}"
        return msg.format(self.centro, self.radio, self.listaPuntos)