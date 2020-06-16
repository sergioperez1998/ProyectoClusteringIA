import tkinter as tk
from functools import partial
from tkinter import filedialog, Menu, Listbox, END, Frame, messagebox, Label, Entry, Radiobutton,\
    IntVar, Toplevel, scrolledtext, INSERT
from tkinter import ttk
from codigo.clustering import clustering
from codigo.circunferencia import Circunferencia
from codigo.punto import Punto


def openFile():
    global path
    try:
        path = filedialog.askopenfilename(filetypes=(("Archivos csv", "*.csv"), ("All files", "*.*")))
        ruta = 'Datos de entrada: ' + path.split('/')[-1]
        listbox.delete(1)
        listbox.insert(1, ruta)
    except:
        messagebox.showinfo('Alerta', 'No se ha cargado correctamente el archivo.')



def mostrar_resultados(datos_salida):
    ventana_resultdos = Toplevel()
    ventana_resultdos.title('Resultados del algoritmo')
    ventana_resultdos.geometry('700x350+300+300')

    tab_control = ttk.Notebook(ventana_resultdos)

    tab1 = tk.Frame(tab_control)
    tab_control.add(tab1, text='Estadísticas generales')
    tab2 = tk.Frame(tab_control)
    tab_control.add(tab2, text='Clusters')

    title_frame = Frame(tab1)
    title_frame.pack()
    label_titulo = ttk.Label(title_frame, text="Resultados generales")
    label_titulo.place(x=25, y=25, anchor="center")
    label_titulo.grid(row=0, column=0, pady=10)
    label_titulo.config(font=('Verdana', 15))

    title2_frame = Frame(tab2)
    title2_frame.pack()
    label2_titulo = ttk.Label(title2_frame, text="Datos de los clusters")
    label2_titulo.place(x=25, y=25, anchor="center")
    label2_titulo.grid(row=0, column=0, pady=10)
    label2_titulo.config(font=('Verdana', 15))

    num_pruebas_realizadas = datos_salida[0]
    tiempo_ejecucion = round(datos_salida[1], 8)
    min_ptos_sin_asignar = datos_salida[2]
    max_ptos_sin_asignar = datos_salida[3]
    media_ptos_sin_asignar = datos_salida[4]
    iteraciones_resultado= datos_salida[6]
    puntos_sin_asignar = datos_salida[7]

    result_frame = Frame(tab1)
    result_frame.pack()
    resultado = scrolledtext.ScrolledText(result_frame, width=40, height=6)
    resultado.insert(INSERT, 'Número de pruebas realizas: ' + str(num_pruebas_realizadas) + '\n')
    resultado.insert(INSERT, 'Tiempo de ejecución: ' + str(tiempo_ejecucion) + " segundos" + '\n')
    resultado.insert(INSERT, 'Mínimo de puntos sin asignar: ' + str(min_ptos_sin_asignar) + '\n')
    resultado.insert(INSERT, 'Máximo de puntos sin asignar: ' + str(max_ptos_sin_asignar) + '\n')
    resultado.insert(INSERT, 'Media de puntos sin asignar: ' + str(media_ptos_sin_asignar) + '\n')
    resultado.grid(column=0, row=0)
    cancelar_frame = Frame(tab1)
    cancelar = tk.Button(cancelar_frame, font=("Verdana", 10), text="Salir",
                         command=ventana_resultdos.destroy).grid(row=0, column=0, pady=10)
    cancelar_frame.pack()


    result2_frame = Frame(tab2)
    result2_frame.pack()
    resultado_clusters = scrolledtext.ScrolledText(result2_frame, width=40, height=12)
    clusters = datos_salida[5]
    contador_puntos = 1
    resultado_clusters.insert(INSERT, 'Iteraciones del resultado elegido: ' + str(iteraciones_resultado) + '\n')
    resultado_clusters.insert(INSERT, 'Puntos sin asignar: ' + str(puntos_sin_asignar) + '\n'+'\n')

    for index, n in enumerate(clusters, start= 0):
        resultado_clusters.insert(INSERT, '----------------Cluster '+str(index+1)+"---------------"+ '\n')
        resultado_clusters.insert(INSERT, 'Centro: ' + str(n.get_centro()) + '\n')
        resultado_clusters.insert(INSERT, 'Radio: ' + str(n.get_radio()) + '\n')
        puntos_asignados_cluster = n.get_lista_puntos()
        resultado_clusters.insert(INSERT, 'Puntos asignados: ' + str(len(puntos_asignados_cluster)) + '\n')
        cadena_puntos = ''
        for index2, p in enumerate(puntos_asignados_cluster, start=1):
            if index2 % 4:
                cadena_puntos = cadena_puntos + p.__str__()
            else:
                cadena_puntos = cadena_puntos + p.__str__() + "\n"
        resultado_clusters.insert(INSERT, 'Lista de puntos asignados: ' +"\n" + cadena_puntos + '\n')
        resultado_clusters.insert(INSERT, '\n')
    resultado_clusters.grid(column=0, row=0)

    cancelar_frame2 = Frame(tab2)
    cancelar2 = tk.Button(cancelar_frame2, font=("Verdana", 10), text="Salir",
                         command=ventana_resultdos.destroy).grid(row=0, column=0, pady=10)
    cancelar_frame2.pack()

    tab_control.pack(expand=1, fill='both')
    print(datos_salida)




contador = 0
def crear_circunferencia(cuadro_coordenada_x,cuadro_coordenada_y,cuadro_radio, ventana_clusters):
    global contador
    coordenada_x = cuadro_coordenada_x.get()
    coordenada_y = cuadro_coordenada_y.get()
    radio = cuadro_radio.get()
    circunferencias_entrada.append(Circunferencia(Punto(float(coordenada_x),float(coordenada_y)), float(radio)))
    ventana_clusters.destroy()
    contador = contador + 1
    if contador < num_clusters:
        clustering_manual()
    else:
        try:
            datos_salida = clustering(num_iteraciones_totales, path, input_var, num_clusters, criterio_de_parada, iteraciones,
                       circunferencias_entrada)
            mostrar_resultados(datos_salida)
        except:
            messagebox.showinfo('Alerta', 'Configure correctamente las variables para realizar el algoritmo.')

def clustering_automatico():
    global input_var
    input_var = 1
    try:
        datos_salida = clustering(num_iteraciones_totales, path, input_var, num_clusters, criterio_de_parada, iteraciones, circunferencias_entrada)
        mostrar_resultados(datos_salida)
    except:
        messagebox.showinfo('Alerta', 'Configure correctamente las variables para realizar el algoritmo.')

def clustering_manual():
    global contador
    global input_var
    input_var = 0
    if '/' in path and num_clusters != 0 and num_iteraciones_totales > 0 and iteraciones >= 0:
        ventana_clusters = Toplevel()
        ventana_clusters.title('Introducir circunferencia inicial')
        ventana_clusters.geometry('500x300+300+300')
        miFrame = Frame(ventana_clusters, width=50, height=50)
        miFrame.pack()
        label_clusters = Label(miFrame, text="Datos de la circunferencia: "+str(contador+1))
        label_clusters.place(x=25, y=25, anchor="center")
        label_clusters.grid(row=0, column=0)
        label_clusters.config(font=('Verdana', 15))

        clusters_manual = Frame(ventana_clusters)
        coordenada_x = Label(clusters_manual, text="Centro - Coordenada X:", font=('Verdana', 9)).grid(row=0, column=0)
        cuadro_coordenada_x = Entry(clusters_manual)
        cuadro_coordenada_x.grid(row=0, column=1)
        coordenada_y = Label(clusters_manual, text="Centro - Coordenada Y:", font=('Verdana', 9)).grid(row=1, column=0)
        cuadro_coordenada_y = Entry(clusters_manual)
        cuadro_coordenada_y.grid(row=1, column=1)
        radio = Label(clusters_manual, text="Radio:", font=('Verdana', 9)).grid(row=2, column=0)
        cuadro_radio = Entry(clusters_manual)
        cuadro_radio.grid(row=2, column=1)
        clusters_manual.pack()

        btn_coordenadas = Frame(ventana_clusters)
        aceptar = tk.Button(btn_coordenadas, font=("Verdana", 11), text="Aceptar",command=partial(crear_circunferencia,
                            cuadro_coordenada_x, cuadro_coordenada_y, cuadro_radio,ventana_clusters)).grid(row=0, column=0)
        btn_coordenadas.pack()
    else:
        messagebox.showinfo('Alerta', 'Introduzca las variables para realizar el algoritmo.')


def actualizar_variables(cuadro_num_clusters, cuadro_num_iteraciones_algoritmo, radioValue, cuadro_num_iteraciones, ventana_configuracion):
    global num_clusters
    global num_iteraciones_totales
    global criterio_de_parada
    global iteraciones

    criterio_de_parada = int(radioValue.get())
    try:
        num_clusters = int(cuadro_num_clusters.get())
        num_iteraciones_totales = int(cuadro_num_iteraciones_algoritmo.get())
        if criterio_de_parada == 0:
            iteraciones = int(cuadro_num_iteraciones.get())
            assert iteraciones > 0
        actualizar(listbox)
        ventana_configuracion.destroy()
    except ValueError:
        messagebox.showinfo('Alerta', 'Introduce un numero.')
    except AssertionError:
        messagebox.showinfo('Alerta', 'Numero de iteraciones por clusters es obligatorio para el criterio de iteraciones.')


def configuracion():
    ventana_configuracion = Toplevel()
    ventana_configuracion.title('Configuración de variables')
    ventana_configuracion.geometry('650x300+300+300')
    miFrame = Frame(ventana_configuracion, width=50,height=50)
    miFrame.pack()
    label_configuracion = Label(miFrame, text="Configuración de variables")
    label_configuracion.place(x=25, y=25, anchor="center")
    label_configuracion.grid(row=0, column=0)
    label_configuracion.config(font=('Verdana', 15))

    formulario = Frame(ventana_configuracion)

    variables_obligatorias = Frame(ventana_configuracion)
    label_obligatorios = Label(variables_obligatorias, text="El campo es obligatorio **", fg="red")
    label_obligatorios.grid(row=0, column=0)
    label_obligatorios.config(padx=10, pady=10, font=('Verdana', 9))
    variables_obligatorias.pack()

    label_num_clusters = Label(formulario, text="Número de clusters: **")
    label_num_clusters.grid(row=1, column=0)
    label_num_clusters.config(padx=10, pady=10, font=('Verdana', 9))
    cuadro_num_clusters = Entry(formulario)
    cuadro_num_clusters.grid(row=1, column=1)

    label_num_iteraciones_algoritmo = Label(formulario, text="Número de pruebas a realizar: **")
    label_num_iteraciones_algoritmo.grid(row=2, column=0)
    label_num_iteraciones_algoritmo.config(padx=10, pady=10, font=('Verdana', 9))
    cuadro_num_iteraciones_algoritmo = Entry(formulario)
    cuadro_num_iteraciones_algoritmo.grid(row=2, column=1)

    label_num_iteraciones = Label(formulario, text="Número de iteraciones: ")
    label_num_iteraciones.grid(row=3, column=0)
    label_num_iteraciones.config(padx=10, pady=10, font=('Verdana', 9))
    cuadro_num_iteraciones = Entry(formulario)
    cuadro_num_iteraciones.grid(row=3, column=1)

    radioValue = IntVar()
    Radiobutton(formulario, font=('Verdana', 9), text="Criterio de iteraciones", variable=radioValue,
                value=0).grid(row=4, column=0)
    Radiobutton(formulario, font=('Verdana', 9), text="Criterio de similitud", variable=radioValue,
                value=1).grid(row=4, column=1)
    formulario.pack()

    configuracion_botones = Frame(ventana_configuracion)
    aceptar = tk.Button(configuracion_botones, font=("Verdana", 11), text="Aceptar",
                                 command=partial(actualizar_variables, cuadro_num_clusters,
                                 cuadro_num_iteraciones_algoritmo, radioValue, cuadro_num_iteraciones, ventana_configuracion)).grid(row=0, column=0)
    cancelar = tk.Button(configuracion_botones, font=("Verdana", 11), text="Cancelar", command=ventana_configuracion.destroy).grid(row=0, column=1)
    configuracion_botones.pack()


def actualizar(listbox):
    iteraciones_totales = "Número de pruebas a realizar: " + str(num_iteraciones_totales)
    listbox.delete(0)
    listbox.insert(0, iteraciones_totales)
    ruta = 'Datos de entrada: '+ path.split('/')[-1]
    listbox.delete(1)
    listbox.insert(1, ruta)
    clusters = "Número de clusters: " + str(num_clusters)
    listbox.delete(2)
    listbox.insert(2, clusters)
    criterio_parada = "Criterio de parada: "+ criterios[int(criterio_de_parada)]
    listbox.delete(3)
    listbox.insert(3, criterio_parada)
    iteraciones_criterio_i = "Número de iteraciones: " + str(iteraciones)
    listbox.delete(4)
    listbox.insert(4, iteraciones_criterio_i)


if __name__ == "__main__":

    root = tk.Tk()
    root.title('Proyecto IA 2020 - Clustering Bajo Incertidumbre')
    root.geometry('650x300+300+300')

    path = ''
    num_clusters = 0
    num_iteraciones_totales = 100 #100 Iteraciones del algoritmo por defecto
    similitud_cluster = True
    criterios= ['Criterio de iteraciones', 'Criterio de similitud']
    criterio_de_parada= 1 #Por defecto esta activado el criterio de similitud --> 0 criterio de iteraciones
    iteraciones = 0 # 100 iteraciones por defecto
    input_var = 1 # Modo automatico, 0 --> Modo manual
    circunferencias_entrada = []

    menu = Menu(root)
    menu.add_command(label='Seleccionar CSV', command=openFile)
    menu.add_command(label='Configurar variables', command=configuracion)
    root.config(menu=menu)

    inicio = Frame(root)
    label_inicio = Label(inicio, text="Variables de ejecución")
    label_inicio.grid(row=0, column=0, pady=10)
    label_inicio.config(font=('Verdana', 15))
    inicio.pack()

    global listbox
    listbox = Listbox(root, font=("Verdana", 9), width=40, height=5)
    listbox.pack()
    for item in ["Número de pruebas a realizar: ", "Datos de entrada: ", "Número de clusters: ",
                 "Criterio de parada: ", "Número de iteraciones: "]:
        listbox.insert(END, item)

    botones = Frame(root)
    f_automatica = tk.Button(botones, font=("Verdana", 10), text="Inicialización Automática", command=clustering_automatico).grid(row=0, column=0, pady=10)
    f_manual = tk.Button(botones, font=("Verdana", 10), text="Inicialización Manual", command=clustering_manual).grid(row=0, column=1, pady=10, padx=10)
    salir = Frame(root)
    cancelar = tk.Button(salir, font=("Verdana", 10), text="Salir",
                         command=root.destroy).grid(row=0, column=0, pady=10)
    botones.pack()
    salir.pack()


root.mainloop()