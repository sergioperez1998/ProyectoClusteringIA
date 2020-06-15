# Proyecto Clustering IA 2020

Este es el código del proyecto de Clustering para la asignatura IA del curso 2020.
El proyecto consiste en un algoritmo que reconozca patrones de circunferencias en nubes de puntos dadas como archivos CSV.

## 1. Instalación

Para que el código funcione correctamente se necesitarán instalar los requisitos del proyecto.

```bash
pip install -r requirements.txt
```

## 2. Uso
#### 2.1 Consola

```cmd
python consola.py --help
usage: Proyecto Clustering IA 2020 [-h] -np NP -de DE -i {0,1} -nc NC -cp {0,1} [-ni NI]

Interfaz de consola del Proyecto de Clustering IA 2020.

optional arguments:
  -h, --help            show this help message and exit
  -np NP, -numeroPruebas NP
                        Número de pruebas a realizar.
  -de DE, -datosEntrada DE
                        Ruta completa del csv de entrada.
  -i {0,1}, -inicializacion {0,1}
                        Modo de inicialización.
                                 Si elige 0 tendrá que introducir a mano el centro y radio de las circunferencias.
                                 Si elige el modo 1 se generarán automáticamente.
  -nc NC, -numeroCluster NC
                        Número de cluster iniciales.
  -cp {0,1}, -criterioParada {0,1}
                        Criterio de parada.
                                 Si elige 0 tendrá que añadir el parámero -ni con el número de iteraciones a parar.
                                 Si elige el modo 1 se utilizará el criterio de similitud de clúster.
  -ni NI, -numeroIteraciones NI
                        Número de iteraciones si se elige el criterio de parada por iteraciones
```

##### 2.1.1 Ejemplo
En este ejemplo se realiza una prueba 100 veces, con los datos del archivo "datos.csv", con 3 clusters que se inicializan de forma automática y con el criterio de parada de similitud.
```cmd
consola.py -np 100 -de "C:\ruta\datos.csv" -i 1 -nc 3 -cp 1
```

### 2.2. Interfaz gráfica


## 3. Licencia
[MIT](https://choosealicense.com/licenses/mit/)