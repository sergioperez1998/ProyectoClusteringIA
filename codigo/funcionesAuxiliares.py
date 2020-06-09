import csv
from codigo.punto import Punto
from codigo.circunferencia import Circunferencia
from math import sqrt, dist
import numpy as np
import operator

# Método para leer los datos de entrada, provenientes de un archivo csv.
def leer_datos(path):
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        listado_puntos = []
        for row in csv_reader:
            x = Punto(float(row[0]), float(row[1]))
            listado_puntos.append(x)
    return listado_puntos


# Objetivo específico 2 - Método Local: Aproximación basada en tres puntos alejados entre sí.
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

    return Circunferencia(centro, radio)


# Objetivo específico 3 - Calculo de los grados de pertenencia de un punto a un conjunto de clusters.
def grado_pertenencia(punto, circunferencias):
    grados_punto = []
    distancias_punto = []
    for circunferencia in circunferencias:
        a = np.array((punto.get_x(), punto.get_y()))
        b = np.array((circunferencia.get_centro().get_x(), circunferencia.get_centro().get_y()))
        dist_centro = abs(np.linalg.norm(a-b) - circunferencia.get_radio())

        if dist_centro != 0:
            inv_prop = (1 / dist_centro)
            grados_punto.append(inv_prop)
            distancias_punto.append(dist_centro)
        else:
            grados_punto.append(1)
            distancias_punto.append(0)

        # print("-------------------------------")
        # print(dist_centro)
        # print(inv_prop)
        # print("-------------------------------")

    grados_normalizados = [i / sum(grados_punto) for i in grados_punto]

    # print("-------------------------------")
    # print(punto.__str__())
    # print(grados_punto)
    # print(grados_normalizados)
    # print("-------------------------------")

    punto.grado_pertenencia = grados_normalizados
    punto.distancias = distancias_punto


def actualizar_cluster(circunferencias, puntos):
    for index, cluster in enumerate(circunferencias, start=0):
        n_centro = []
        for j in puntos:
            if j.get_grado_pertenencia()[index] > 0.20:
                #print(j.__str__())
                n_centro.append(j)

        cluster.centro = Punto(sum(p.get_x() for p in n_centro)/len(n_centro), sum(p.get_y() for p in n_centro)/len(n_centro))

        d_centro = []
        for k in n_centro:
            a = np.array((k.get_x(), k.get_y()))
            b = np.array((cluster.get_centro().get_x(), cluster.get_centro().get_y()))
            dist_centro = abs(np.linalg.norm(a - b))
            d_centro.append(dist_centro)

        cluster.radio = sum(d_centro)/len(d_centro)

        print(index)
        print(cluster.get_centro())
        print(cluster.get_radio())
        print("------------------")

def asignar_puntos2(circunferencias, puntos):
    for p in puntos:
        max_value = max(p.get_grado_pertenencia())
        max_index = p.get_grado_pertenencia().index(max_value)
        circunferencias[max_index].get_lista_puntos().append(p)































# Objetivo específico 2 - Método Local: Aproximación basada en tres puntos alejados entre sí.
def encontrar_circulo2(punto1, punto2, punto3):
    A = np.array([punto1.get_x(), punto1.get_y()])
    B = np.array([punto2.get_x(), punto2.get_y()])
    C = np.array([punto3.get_x(), punto3.get_y()])
    a = np.linalg.norm(C - B)
    b = np.linalg.norm(C - A)
    c = np.linalg.norm(B - A)
    s = (a + b + c) / 2
    R = a * b * c / 4 / np.sqrt(s * (s - a) * (s - b) * (s - c))
    b1 = a * a * (b * b + c * c - a * a)
    b2 = b * b * (a * a + c * c - b * b)
    b3 = c * c * (a * a + b * b - c * c)
    P = np.column_stack((A, B, C)).dot(np.hstack((b1, b2, b3)))
    P /= b1 + b2 + b3
    print(P)

    print("-------------------------------")
    print("Centro = (", P.get_x(), ", ", P.get_y(), ")")
    print("Radio = ", R)
    print("-------------------------------")

    return Circunferencia(P, R)


# Objetivo específico 3 - Calculo de los grados de pertenencia de un punto a un conjunto de clusters.
def grado_pertenencia2(punto, circunferencias):
    grados_punto = []
    for circunferencia in circunferencias:
        a = np.array((punto.get_x(), punto.get_y()))
        b = np.array((circunferencia.get_centro().get_x(), circunferencia.get_centro().get_y()))
        dist_centro = abs(np.linalg.norm(a-b) - circunferencia.get_radio())

        if dist_centro != 0:
            inv_prop = (1 / dist_centro)
            grados_punto.append(inv_prop)
        else:
            grados_punto.append(1)

    grados_normalizados = [i / sum(grados_punto) for i in grados_punto]
    punto.grado_pertenencia = grados_normalizados


def actualizar_cluster2(circunferencias, puntos):
    for index, cluster in enumerate(circunferencias, start=0):
        n_centro = []
        for j in puntos:
            if j.get_grado_pertenencia()[index] > 1/len(circunferencias):
                n_centro.append(j)

        cluster.centro = Punto(sum(p.get_x() for p in n_centro)/len(n_centro), sum(p.get_y() for p in n_centro)/len(n_centro))

        d_centro = []
        for k in n_centro:
            a = np.array((k.get_x(), k.get_y()))
            b = np.array((cluster.get_centro().get_x(), cluster.get_centro().get_y()))
            dist_centro = abs(np.linalg.norm(a - b))
            d_centro.append(dist_centro)

        cluster.radio = sum(d_centro)/len(d_centro)

        ################################################################



        print(index)
        print(cluster.get_centro())
        print(cluster.get_radio())
        print("------------------")