from codigo.funcionesAuxiliares import *
from codigo.circunferencia import Circunferencia
import random
import matplotlib.pyplot as plt
import numpy

# 1. Inicialización de circunferencias iniciales (centro y radio de cada una)
# 2. Repetir (hasta condición de parada)
# 2.1. actualizar grados de pertenencia de los puntos a las circunferencias
# 2.2. actualizar centros y radios
# 3. Asignar cada punto únicamente a su cluster de mayor grado de pertenencia,
# y devolver la información completa para cada cluster (centro, radio y lista de puntos asignados a él).

# 0. Leer datos
datos_entrada = leer_datos('../data/entrada-profesor.csv')

min_x_value = min(p.get_x() for p in datos_entrada)
max_x_value = max(p.get_x() for p in datos_entrada)
min_y_value = min(p.get_y() for p in datos_entrada)
max_y_value = max(p.get_y() for p in datos_entrada)

# 1. Inicialización de circunferencias iniciales (centro y radio de cada una)
tres_puntos = random.sample(datos_entrada, 3)
circulo = encontrar_circulo(tres_puntos[0], tres_puntos[1], tres_puntos[2])

tres_puntos2 = random.sample(datos_entrada, 3)
circulo2 = encontrar_circulo(tres_puntos2[0], tres_puntos2[1], tres_puntos2[2])

# random.seed(82948293048923432)
# tres_puntos3 = random.sample(datos_entrada, 3)
# circulo3 = encontrar_circulo(tres_puntos3[0], tres_puntos3[1], tres_puntos3[2])

# circulo = encontrar_circulo(Punto(2, 6), Punto(6, 7), Punto(4, 6))
# circulo2 = encontrar_circulo(Punto(8, 1), Punto(10, 2), Punto(6, 7))

circunferencias = [circulo, circulo2]
# 2. Repetir (hasta condición de parada)
# 2.1. actualizar grados de pertenencia de los puntos a las circunferencias


for z in range(100):
    for i in datos_entrada:
        grado_pertenencia(i, circunferencias)

    # 2.2. actualizar centros y radios
    actualizar_cluster2(circunferencias, datos_entrada)

# 3. Asignar cada punto únicamente a su cluster de mayor grado de pertenencia,
asignar_puntos(circunferencias, datos_entrada)

x = []
y = []
for i in datos_entrada:
    x.append(i.get_x())
    y.append(i.get_y())

plt.plot(x, y, 'o', color='black')

for c in circunferencias:
    print("-----------")
    print("Centro: " + c.centro.__str__())
    print("Radio: " + str(c.get_radio()))
    print("".join([p.__str__() for p in c.get_lista_puntos()]))
    circle = plt.Circle([c.get_centro().get_x(), c.get_centro().get_y()], radius=c.get_radio(), facecolor='none',
                        edgecolor=numpy.random.rand(3, ))
    plt.gcf().gca().add_artist(circle)

plt.show()
