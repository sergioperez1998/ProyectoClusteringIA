import random
import numpy as np
import csv
import matplotlib.pyplot as plt


def circulos_aleatorios(max_x, max_y, max_radio, num_circunferencias, archivo):
    with open(archivo, 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(num_circunferencias):
            radio = random.randint(1, max_radio)
            num_puntos = random.randint(5, 30)
            centro = [random.randint(1, max_x), random.randint(1, max_y)]
            puntos = np.linspace(0, 2 * np.pi, num_puntos)
            x = centro[0] + radio * np.cos(puntos)
            y = centro[1] + radio * np.sin(puntos)

            for j in range(num_puntos):
                writer.writerow([x[j], y[j]])


def circulos_pseudo_aleatorios(circulos, max_radio, archivo):
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


# circulos_aleatorios(30, 30, 20, 5, 'test.csv')
circulos = []
for z in range(5):
    circulos.append([random.randint(1, 50), random.randint(1, 50)])
circulos_pseudo_aleatorios(circulos, 12, 'C:\\Users\\adria\\PycharmProjects\\ProyectoClustering\\data\\test.csv')
