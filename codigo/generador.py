import random
import numpy as np
import csv
import matplotlib.pyplot as plt

#Método que genera circunferencias dados una lista de puntos, un radio maximo y la ruta para guardar el resultado
def circunferencias_pseudo_aleatorias(circulos, max_radio, archivo):
    x_datos = []
    y_datos = []
    with open(archivo, 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(len(circulos)):
            radio = random.randint(5, max_radio)
            num_puntos = random.randint(8, 30)
            puntos = np.linspace(0, 2 * np.pi, num_puntos)
            x = circulos[i][0] + radio * np.cos(puntos)
            y = circulos[i][1] + radio * np.sin(puntos)

            for j in range(num_puntos):
                writer.writerow([x[j], y[j]])

                x_datos.append(x[j])
                y_datos.append(y[j])

    plt.plot(x_datos, y_datos, 'o', color='black')
    plt.show()


num_cluster = 5
circulos = []
max_radio = 10
for z in range(num_cluster):
    circulos.append([random.randint(1, 50), random.randint(1, 50)])

#Poner la ruta específica para guardar el resultado.
circunferencias_pseudo_aleatorias(circulos, max_radio, 'C:\\Users\\adria\\PycharmProjects\\ProyectoClustering\\data\\test.csv')
