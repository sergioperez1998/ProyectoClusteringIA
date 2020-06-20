# Estructura del código fuente

El código del proyecto se estructura de la siguiente forma:

proyecto-clustering-ia-2020/
├── codigo/
│   ├── __init__.py
│   ├── circunferencia.py
│   ├── clustering.py
│   ├── funcionesAuxiliares.py
│   ├── generador.py
│   └── punto.py
├── data/
│   ├── entrada-2-circunferencias.csv
│   ├── entrada-3-circunferencias.csv
│   └── entrada-5-circunferencias.csv
├── consola.py
├── interfaz.py
├── README.txt
└── requirements.txt

En esta carpeta 'proyecto-clustering-ia-2020' se encuentra por orden alfabético:

1. La carpeta codigo, esta carpeta contiene el código principal del proyecto, se compone de los siguientes archivos:
 - __init.py__ : Archivo necesario para la correcta llamada de funciones entre los diferentes archivos .py
 - circunferencia.py : Este archivo contiene la clase 'Circunferencia', que es la representación de los clústeres.
 - clustering.py : Este archivo contiene la función principal, es la que recibe todos los datos y ejecuta todos los métodos necesarios y devuelve los resultados.
 - funcionesAuxiliares.py : Este archivo contiene todas las funciones necesarías para la ejecución del proyecto, son llamadas desde el archivo clustering.py
 - generador.py : Un pequeño generador de datos de entrada, contiene una función que recibe el número de circunferencias a generar, y el radio máximo de estas, devuelve un archivo .csv con puntos aleatorios pertenecientes a las circunferencias generadas.
 - punto.py : Este archivo contiene la clase 'Punto', que es la representación de los puntos de los datos de entrada.

2. La carpeta data, esta carpeta contiene los archivos de entrada usados para la experimentación del proyecto, se compone de los siguientes archivos:
 - entrada-2-circunferencias.csv : Contiene 16 puntos que representan 2 circunferencias.
 - entrada-3-circunferencias.csv : Contiene 79 puntos que representan 3 circunferencias.
 - entrada-5-circunferencias.csv : Contiene 101 puntos que representan 5 circunferencias.

3. consola.py : Este archivo es el que se encarga de recibir los parámetros por consola y llamar a la función del archivo clustering.py para ejecutarlo, siriviendo así de forma de ejecutar los experimentos.

4. interfaz.py : Este archivo ejecuta y muestra la interfaz de usuario, desde donde se pueden realizar pruebas de forma más intuitiva y cómoda para el usuario.

5. README.txt : Este mismo archivo en el cuál se explica la estructura del código, formato de los datos de entrada, uso de la interfaz, uso de la consola y reproducción de los experimentos realizados.

6. requirements.txt : Archivo que contiene los requisitos para ejecutar el resto de archivos, para su utilización basta con escribir el comando 'pip install -r requirements.txt'. PD: Este proyecto ha sido realizado y probado sobre Python 3.8 sobre el SO Windows 10.

#Datos de entrada

El proyecto recibe como archivo de entrada un archivo de extensión CSV dividido en dos columnas sin encabezado, en la primera columna estará la coordenada x, seguido de una coma, que separara este primer valor de la segunda columna que será la coordenada y. Si se desea ver un ejemplo de este formato, puede consultarse cualquiera de los archivos CSV que se encuentran en la carpeta 'data'.

# Uso de la interfaz

1. Para utilizar la interfaz se debe ejecutar el archivo interfaz.py, esto mostrará una ventana de título 'Proyecto IA 2020 - Clustering Bajo Incertidumbre'.
2. Seleccione el archivo CSV de datos de entrada pinchando en la barra de menú superior en 'Seleccionar CSV', seleccione el archivo y pulse el botón 'Abrir'.
3. Configure las variables de ejecución pinchando en la barra de menú superior en 'Configurar variables', rellene todos los campos obligatorios, el campo 'Número de iteraciones' solo tendrá que ser rellenado en el caso de que se seleccione la opción de 'Criterio de iteraciones'. Por último, pulse el botón 'Aceptar'.
4. En la caja blanca se mostrarán todas las variables y el archivo de entrada que ha seleccionado, a continuación pulse 'Inicialización Automática' si desea que las circunferencias iniciales se generen solas, o 'Inicialización Manual' si desea introducir manualmente los centros y radios de las circunferencias iniciales, en este caso, se abrirá una ventana donde tendrá que introducir la coordenada x, y y el radio de la circunferencia.
5. Una vez pulsado el botón 'Inicialización Automática' o termine de rellenar las circunferencias iniciales, se mostrará la misma ventana hasta que acabe la ejecución el algoritmo, en ese momento aparecerá otra ventana llamada 'Resultados del algoritmo'.
6. En la ventana de los resultados verá dos pestañas. La primera 'Estadísticas generales' le mostrará información general sobre la prueba realizada, en la segunda pestaña 'Clústeres', encontrará información sobre el mejor resultado devuelto por el algoritmo.
7. En ambas pestañas encontrará un botón 'Mostrar gráfica' que abrirá una ventana con una gráfica representando el resultado devuelto por el algoritmo.

# Uso de la consola de comando

1. Para realizar experimentos por consola tendrá que ejecutar el archivo consola.py seguido de ciertos parámetros, estos parámetros son:
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

2. Por ejemplo, en el caso de querer ejecutar una prueba 100 veces, sobre el archivo 'entradas-2-circunferencias.csv', con inicialización automática, 2 clústeres y criterio de parada por similitud, deberé ejecutar lo siguiente:
 - python consola.py -np 100 -de "C:\ruta\data\entradas-2-circunferencias.csv" -i 1 -nc 2 -cp 1

3. Esto devolverá en consola los resultados obtenidos, y una ventana con la gráfica del resultado.

4. En caso de que el modo de inicialización sea manual, se le pedirá por consola que introduzca los datos necesarios.

# Reproducción de los experimentos realizados

En el apartado anterior se ha indicado como realizar pruebas, en este apartado se pondrán algunos ejemplos de los argumentos utilizados para la realización de algunas de las pruebas del proyecto:

1. Prueba #3
 - python consola.py -np 1000 -de "C:\ruta\data\entradas-2-circunferencias.csv" -i 1 -nc 2 -cp 0 -ni 1000 

2. Prueba #4
 - python consola.py -np 1000 -de "C:\ruta\data\entradas-2-circunferencias.csv" -i 1 -nc 2 -cp 1

3. Prueba #9
 - python consola.py -np 500 -de "C:\ruta\data\entradas-3-circunferencias.csv" -i 1 -nc 2 -cp 0 -ni 500

4. Prueba #10
 - python consola.py -np 1000 -de "C:\ruta\data\entradas-3-circunferencias.csv" -i 1 -nc 2 -cp 1

5. Prueba #17
 - python consola.py -np 500 -de "C:\ruta\data\entradas-5-circunferencias.csv" -i 1 -nc 2 -cp 0 -ni 500 

6. Prueba #18
 - python consola.py -np 500 -de "C:\ruta\data\entradas-5-circunferencias.csv" -i 1 -nc 2 -cp 1

Para el resto de pruebas se seguiría la misma estructura modificando las entradas como se indica en las tablas del documento.

* En el documento se indica al final de los resultados, que con lo obtenido en los experimentos, se ha establecido el umbral por defecto en el 15%, en el caso de querer modificar este umbral, se deberá modificar en el archivo 'funcionesAuxiliares.py' las líneas 235 y 236. Estas líneas contienen las variables 'radio_arriba' y 'radio_abajo'. Con un umbral del 15% estás variables tienen asignados los valores '1.15' y '0.85', en el caso de querer probar por ejemplo el umbral 25%, deberá ajustar estos valores a '1.25' y '0.75' respectivamente, y así con el umbral que se desee probar.

