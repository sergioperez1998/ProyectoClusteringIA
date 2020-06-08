import csv
from codigo.punto import Punto
from math import sqrt, dist


# Leer datos de entrada
def leer_datos(path):
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        listado_puntos = []
        for row in csv_reader:
            x = Punto(int(row[0]), int(row[1]))
            # print(x)
            listado_puntos.append(x)

    return listado_puntos


# Método Local 1 - Aproximación basada en tres puntos alejados entre si
def encontrar_circulo(punto1, punto2, punto3):
    x12 = punto1.get_x() - punto2.get_x()
    x13 = punto1.get_x() - punto3.get_x()

    y12 = punto1.get_y() - punto2.get_y()
    y13 = punto1.get_y() - punto3.get_y()

    y31 = punto3.get_y() - punto1.get_y()
    y21 = punto2.get_y() - punto1.get_y()

    x31 = punto3.get_x() - punto1.get_x()
    x21 = punto2.get_x() - punto1.get_x()

    # x1^2 - x3^2
    sx13 = pow(punto1.get_x(), 2) - pow(punto3.get_x(), 2)

    # y1^2 - y3^2
    sy13 = pow(punto1.get_y(), 2) - pow(punto3.get_y(), 2)

    sx21 = pow(punto2.get_x(), 2) - pow(punto1.get_x(), 2)
    sy21 = pow(punto2.get_y(), 2) - pow(punto1.get_y(), 2)

    f = ((sx13 * x12 + sy13 *
          x12 + sx21 * x13 +
          sy21 * x13) // (2 *
                          (y31 * x12 - y21 * x13)))

    g = ((sx13 * y12 + sy13 * y12 +
          sx21 * y13 + sy21 * y13) //
         (2 * (x31 * y12 - x21 * y13)))

    c = (-pow(punto1.get_x(), 2) - pow(punto1.get_y(), 2) -
         2 * g * punto1.get_x() - 2 * f * punto1.get_y())

    # eqn of circle be x^2 + y^2 + 2*g*x + 2*f*y + c = 0
    # where centre is (h = -g, k = -f) and
    # radius r as r^2 = h^2 + k^2 - c
    h = -g
    k = -f
    sqr_of_r = h * h + k * k - c

    # r is the radius
    radio = round(sqrt(sqr_of_r), 5)
    centro = Punto(h, k)

    print("-------------------------------")
    print("Centro = (", centro.get_x(), ", ", centro.get_y(), ")")
    print("Radio = ", radio)
    print("-------------------------------")

    return [centro, radio]


def grado_pertenencia(punto1, circunferencias):
    grados_punto = []
    for circunferencia in circunferencias:
        dist_centro = abs(dist([punto1.get_x(), punto1.get_y()], [circunferencia.get_centro().get_x(), circunferencia.get_centro().get_y()]) - circunferencia.get_radio())
        inv_prop = (1/dist_centro)
        grados_punto.append(inv_prop)

        print("-------------------------------")
        print(dist_centro)
        print(inv_prop)
        print("-------------------------------")

    grados_normalizados = [i/sum(grados_punto) for i in grados_punto]

    print("-------------------------------")
    print(grados_punto)
    print("-------------------------------")
    print(grados_normalizados)

