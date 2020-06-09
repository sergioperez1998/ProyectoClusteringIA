from codigo.funcionesAuxiliares import *
from codigo.circunferencia import Circunferencia
import random
import matplotlib.pyplot as plt
import matplotlib.patches as pat


# 1. Inicialización de circunferencias iniciales (centro y radio de cada una)
# 2. Repetir (hasta condición de parada)
# 2.1. actualizar grados de pertenencia de los puntos a las circunferencias
# 2.2. actualizar centros y radios
# 3. Asignar cada punto únicamente a su cluster de mayor grado de pertenencia,
# y devolver la información completa para cada cluster (centro, radio y lista de puntos asignados a él).

# 0. Leer datos
datos_entrada = leer_datos('../data/entrada.csv')

# plt.style.use('seaborn-whitegrid')
# x = []
# y = []
# for i in datos_entrada:
#     x.append(i.get_x())
#     y.append(i.get_y())
#
# plt.plot(x, y, 'o', color='black')
# plt.show()
# 4.4
# 4.12
# 12.4
# 12.12


# 1. Inicialización de circunferencias iniciales (centro y radio de cada una)
# tres_puntos = random.sample(datos_entrada, 3)
# circulo = encontrar_circulo(tres_puntos[0], tres_puntos[1], tres_puntos[2])
# tres_puntos2 = random.sample(datos_entrada, 3)
# circulo2 = encontrar_circulo(tres_puntos2[0], tres_puntos2[1], tres_puntos2[2])

circunferencia = Circunferencia(Punto(5, 2), 3, [])
circunferencia2 = Circunferencia(Punto(3, 1), 4, [])
circunferencia3 = Circunferencia(Punto(13, 7), 2, [])
circunferencia4 = Circunferencia(Punto(10, 15), 5, [])
circunferencia5 = Circunferencia(Punto(7, 6), 1, [])
circunferencia6 = Circunferencia(Punto(14, 11), 6, [])
circunferencia7 = Circunferencia(Punto(6, 15), 9, [])
circunferencia8 = Circunferencia(Punto(10, 1), 7, [])



# 2. Repetir (hasta condición de parada)
# 2.1. actualizar grados de pertenencia de los puntos a las circunferencias
circunferencias = [circunferencia, circunferencia2, circunferencia3, circunferencia4, circunferencia5, circunferencia6, circunferencia7, circunferencia8]

for z in range(10):
    for i in datos_entrada:
        grado_pertenencia(i, circunferencias)

# 2.2. actualizar centros y radios
    actualizar_cluster(circunferencias, datos_entrada)

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
    circle = plt.Circle([c.get_centro().get_x(), c.get_centro().get_y()], radius=c.get_radio())
    plt.gcf().gca().add_artist(circle)

plt.show()
