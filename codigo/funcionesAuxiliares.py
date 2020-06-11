import csv
from codigo.punto import Punto
from codigo.circunferencia import Circunferencia
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
import random


# Método para leer los datos de entrada, provenientes de un archivo csv.
def leer_datos(path):
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        listado_puntos = []
        for row in csv_reader:
            x = Punto(float(row[0]), float(row[1]))
            listado_puntos.append(x)
    return listado_puntos

# Método que parte organiza los datos en 4 cuadrantes y circunferencias aleatorias dependiendo de la posición de los puntos
# y del número de clusters que deseemos para obtener la solución optima.
def inicializar_datos(datos_entrada, num_cluster, circunferencias):
    max_x_value = max(p.get_x() for p in datos_entrada)
    max_y_value = max(p.get_y() for p in datos_entrada)

    med_x_value = int(max_x_value / 2)
    med_y_value = int(max_y_value / 2)

    arriba_izquierda = []
    arriba_derecha = []
    abajo_izquierda = []
    abajo_derecha = []

    for p in datos_entrada:
        if p.get_x() < med_x_value and p.get_y() > med_y_value:
            arriba_izquierda.append(p)
        if p.get_x() > med_x_value and p.get_y() > med_y_value:
            arriba_derecha.append(p)
        if p.get_x() < med_x_value and p.get_y() < med_y_value:
            abajo_izquierda.append(p)
        if p.get_x() > med_x_value and p.get_y() < med_y_value:
            abajo_derecha.append(p)

    cuadrantes = []
    if len(arriba_izquierda) > 3: cuadrantes.append(arriba_izquierda)
    if len(arriba_derecha) > 3: cuadrantes.append(arriba_derecha)
    if len(abajo_izquierda) > 3: cuadrantes.append(abajo_izquierda)
    if len(abajo_derecha) > 3: cuadrantes.append(abajo_derecha)

    cuadrantes.sort(key=len, reverse=True)

    cuadrantes_elegidos = cuadrantes.copy() # abajoIzq  arribaDer
    pesos = [[1.0],[0.80, 0.20],[0.50, 0.30, 0.20],[0.40, 0.30, 0.20, 0.10]]
    if num_cluster > len(cuadrantes_elegidos):
        for i in range(num_cluster-len(cuadrantes_elegidos)):
            cuadrantes_elegidos.append(np.random.choice(cuadrantes_elegidos, 1, replace=False, p=pesos[len(cuadrantes)-1])[0])

    for i in range(num_cluster):
        puntos = np.random.choice(cuadrantes_elegidos[i], 3, replace=False)
        circunferencias.append(encontrar_circulo(puntos[0], puntos[1], puntos[2]))

# Objetivo específico 2 - Método Local: Aproximación basada en tres puntos alejados entre sí.
# Algoritmo para la obtención de circunferencias a partir de 3 puntos dados.
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

    return Circunferencia(centro, radio)


# Objetivo específico 3 - Calculo de los grados de pertenencia de un punto a un conjunto de clusters.
# Calcula el grado de pertenencia de un punto a las circunferencias ya creadas, esto se calcula a partir de la distancia
# de dicho punto al centro de la cada una de las circunferencias.
def grado_pertenencia(punto, circunferencias):
    grados_punto = []
    for circunferencia in circunferencias:
        a = np.array((punto.get_x(), punto.get_y()))
        b = np.array((circunferencia.get_centro().get_x(), circunferencia.get_centro().get_y()))
        dist_centro = abs(np.linalg.norm(a - b) - circunferencia.get_radio())

        if dist_centro != 0:
            inv_prop = (1 / dist_centro)
            grados_punto.append(inv_prop)
        else:
            grados_punto.append(1)

    grados_normalizados = [i / sum(grados_punto) for i in grados_punto]
    punto.grado_pertenencia = grados_normalizados


# Objetivo específico 4 - Actualización de cluster: Centro y radio.
# Se realiza la actualización de cada circunferencia teniendo en cuenta los puntos que tienen un gran grado de pertenencia
# a la misma. Para actualizar los centros se hace la media de valores en X e Y del conjunto de puntos. Y el radio se
# actualiza con la media de distancias de cada punto al centro de la circunferencia.
def actualizar_cluster(circunferencias, puntos):
    for index, cluster in enumerate(circunferencias, start=0):
        n_centro = []
        for j in puntos:
            if j.get_grado_pertenencia()[index] > 1 / len(circunferencias): ######## * 1.2 ?
                n_centro.append(j)

        if len(n_centro) > 0:
            cluster.centro = Punto(sum(p.get_x() for p in n_centro) / len(n_centro),
                                   sum(p.get_y() for p in n_centro) / len(n_centro))

            d_centro = []
            for k in n_centro:
                dist_centro = distancia_centro(k, cluster.get_centro())
                d_centro.append(dist_centro)

            cluster.radio = sum(d_centro) / len(d_centro)


# Criterio básico, se selecciona un numero fijo de iteraciones para realizar el algoritmo
# 1. Lectura y tratamiento de datos
# 2. Calcular grado de pertenencia de cada punto
# 3. Actualizar los clusters
def criterio_iteraciones(numero_iteraciones, datos_entrada, circunferencias):
    iteraciones = 0
    for i in range(numero_iteraciones):
        iteraciones = iteraciones + 1

        for i in datos_entrada:
            # 2.1. actualizar grados de pertenencia de los puntos a las circunferencias
            grado_pertenencia(i, circunferencias)

    # 2.2. actualizar centros y radios
    actualizar_cluster(circunferencias, datos_entrada)

    return iteraciones

# Criterio avanzado, se realiza una copia de los datos anteriores a cada actualización para compararlos a posteriori
# así podemos ver si los clusters se modifican despues de las actualizaciones.
# 1. Lectura y tratamiento de datos
# 2. Calcular grado de pertenencia de cada punto
# 3. Actualizar los clusters
def criterio_similitud(similitud_cluster, circunferencias, datos_entrada):
    iteraciones = 0
    while similitud_cluster:
        iteraciones = iteraciones + 1
        #Creamos una copia de los datos anteriores a la actualización
        tuplas = []
        for c in circunferencias:
            tuplas.append((c.get_centro(), c.get_radio()))

        for i in datos_entrada:
            # 2.1. actualizar grados de pertenencia de los puntos a las circunferencias
            grado_pertenencia(i, circunferencias)

        # 2.2. actualizar centros y radios
        actualizar_cluster(circunferencias, datos_entrada)

        # Comparamos el radio antiguo con el radio nuevo y miramos si la el centro no se ha movido si se da el caso
        # es que esa circunferencia no se ha modificado. En el momento que no se modifiquen ninguna termina el algoritmo.
        criterio = []
        for index, cluster in enumerate(circunferencias, start=0):
            new_centro = cluster.get_centro()
            new_radio = cluster.get_radio()
            old_centro = tuplas[index][0]
            old_radio = tuplas[index][1]
            dist = distancia_centro(new_centro, old_centro)
            if (old_radio * 0.9 < new_radio < old_radio * 1.1) and dist == 0:
                criterio.append(False)
            else:
                criterio.append(True)

        if True not in criterio:
            similitud_cluster = False

    return iteraciones


# Objetivo específico 5 - Asignar puntos y devolver los cluster
# Se asigna cada punto a las circunferencias que mayor grado de pertenencia tenga, obteniendo el centro de la circunferencia
# y calculando la distancia a la misma para así poder comparar si ese punto pertenece a esa circunferencia (si está en el
# rango de +- 25%)
def asignar_puntos(circunferencias, puntos, estadisticas):
    puntos_asignados = 0
    for p in puntos:
        max_value = max(p.get_grado_pertenencia())
        max_index = p.get_grado_pertenencia().index(max_value)
        dist_centro = distancia_centro(p, circunferencias[max_index].get_centro())
        radio = circunferencias[max_index].get_radio()
        radio_arriba = radio * 1.25
        radio_abajo = radio * 0.75
        if radio_abajo < dist_centro < radio_arriba:
            circunferencias[max_index].get_lista_puntos().append(p)
            puntos_asignados = puntos_asignados + 1
    estadisticas.append(len(puntos)-puntos_asignados)

# Se muestran los resultados de cada una de las circunferencias y se dibuja la gráfica.
def mostrar_resultados(datos_entrada, circunferencias, iteraciones):
    x = []
    y = []
    for i in datos_entrada:
        x.append(i.get_x())
        y.append(i.get_y())

    plt.plot(x, y, 'o', color='black')

    # cFinal = []
    # for c in circunferencias:
    #     if len(c.get_lista_puntos()) > 0:
    #         cFinal.append(c)

    print("Iteraciones: " + str(iteraciones))
    for c in circunferencias:
        print("-----------")
        print("Centro: " + c.centro.__str__())
        print("Radio: " + str(c.get_radio()))
        print("".join([p.__str__() for p in c.get_lista_puntos()]))
        colour = np.random.rand(3, )
        circle = plt.Circle((c.get_centro().get_x(), c.get_centro().get_y()), radius=c.get_radio(), facecolor='none',
                            edgecolor=colour)
        for p in c.get_lista_puntos():
            plt.plot(p.get_x(), p.get_y(), marker='s', linestyle='-', color=colour)

        plt.gcf().gca().add_artist(circle)

    plt.show()


# Método para calcular la distancia entre 2 puntos
def distancia_centro(punto1, punto2):
    a = np.array((punto1.get_x(), punto1.get_y()))
    b = np.array((punto2.get_x(), punto2.get_y()))
    dist_centro = abs(np.linalg.norm(a - b))
    return dist_centro