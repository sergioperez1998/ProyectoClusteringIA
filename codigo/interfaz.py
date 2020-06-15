import tkinter as tk
from functools import partial
from tkinter import filedialog, Menu, Listbox, END, Frame, messagebox, Label, Entry, Radiobutton, IntVar, Toplevel


def openFile():
    global path
    path = filedialog.askopenfilename(filetypes=(("Archivos csv", "*.csv"),("All files","*.*")))
    if '/' in path:
        messagebox.showinfo('Notificacion', 'Se ha cargado correctamente el archivo')

def actualizar_variables(cuadro_num_clusters, cuadro_num_iteraciones_algoritmo, radioValue, cuadro_num_iteraciones):
    # Variables a modificar para el algoritmo
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
        messagebox.showinfo('Notificacion', 'Se ha modificado correctamente')
    except ValueError:
        messagebox.showinfo('Alerta', 'Introduce un numero')
    except AssertionError:
        messagebox.showinfo('Alerta', 'Numero de iteraciones por clusters es obligatorio para el criterio de iteraciones')


def configuracion():
    #Ventana para la configuracion de variables
    ventana_configuracion = Toplevel()
    ventana_configuracion.title('Configuracion de variables')
    ventana_configuracion.geometry('500x300+300+300')
    #Frame para crear el formulario con las variables del algoritmo
    miFrame = Frame(ventana_configuracion, width=50,height=50)
    miFrame.pack()
    label_configuracion = Label(miFrame, text="Configuracion de variables")
    label_configuracion.place(x=25, y=25, anchor="center")
    label_configuracion.grid(row=0, column=0)
    label_configuracion.config(font=('Verdana', 15))

    #Frame para formulario
    formulario = Frame(ventana_configuracion)

    variables_obligatorias = Frame(ventana_configuracion)
    label_obligatorios = Label(variables_obligatorias, text="El campo es obligatorio **", fg="red")
    label_obligatorios.grid(row=0, column=0)
    label_obligatorios.config(padx=10, pady=10, font=('Verdana', 9))
    variables_obligatorias.pack()

    #Entrada para el numero de clusters
    label_num_clusters = Label(formulario, text="Numero de clusters: **")
    label_num_clusters.grid(row=1, column=0)
    label_num_clusters.config(padx=10, pady=10, font=('Verdana', 9))
    cuadro_num_clusters = Entry(formulario)
    cuadro_num_clusters.grid(row=1, column=1)

    # Entrada para las iteraciones totales del algoritmo
    label_num_iteraciones_algoritmo = Label(formulario, text="Numero de iteraciones totales: **")
    label_num_iteraciones_algoritmo.grid(row=2, column=0)
    label_num_iteraciones_algoritmo.config(padx=10, pady=10, font=('Verdana', 9))
    cuadro_num_iteraciones_algoritmo = Entry(formulario)
    cuadro_num_iteraciones_algoritmo.grid(row=2, column=1)

    # Entrada para las iteraciones
    label_num_iteraciones = Label(formulario, text="Iteraciones por cluster: ")
    label_num_iteraciones.grid(row=3, column=0)
    label_num_iteraciones.config(padx=10, pady=10, font=('Verdana', 9))
    cuadro_num_iteraciones = Entry(formulario)
    cuadro_num_iteraciones.grid(row=3, column=1)

    #Entrada para el criterio de parada
    radioValue = IntVar()
    Radiobutton(formulario, font=('Verdana', 9), text="Criterio de iteraciones", variable=radioValue,
                value=0).grid(row=4, column=0)
    Radiobutton(formulario, font=('Verdana', 9), text="Criterio de similitud", variable=radioValue,
                value=1).grid(row=4, column=1)
    formulario.pack()

    #Botones
    configuracion_botones = Frame(ventana_configuracion)
    aceptar = tk.Button(configuracion_botones, font=("Verdana", 11), text="Aceptar",
                                 command=partial(actualizar_variables, cuadro_num_clusters,
                                 cuadro_num_iteraciones_algoritmo, radioValue, cuadro_num_iteraciones)).grid(row=0, column=0)
    cancelar = tk.Button(configuracion_botones, font=("Verdana", 11), text="Cancelar", command=ventana_configuracion.destroy).grid(row=0, column=1)
    configuracion_botones.pack()

def actualizar(listbox):

    ruta = 'Archivo: '+ path.split('/')[-1]
    listbox.delete(0)
    listbox.insert(0, ruta)
    clusters = "Numero de clusters: "+ str(num_clusters)
    listbox.delete(1)
    listbox.insert(1, clusters)
    iteraciones_totales = "Iteraciones totales del algoritmo: "+ str(num_iteraciones_totales)
    listbox.delete(2)
    listbox.insert(2, iteraciones_totales)
    iteraciones_criterio_i = "Iteraciones por cluster : " + str(iteraciones)
    listbox.delete(3)
    listbox.insert(3, iteraciones_criterio_i)
    criterio_parada = "Criterio de parada: "+ criterios[int(criterio_de_parada)]
    listbox.delete(4)
    listbox.insert(4, criterio_parada)



if __name__ == "__main__":

    #Ventana principal
    root = tk.Tk()
    root.title('Clustering bajo incertidumbre')
    root.geometry('500x300+300+300')

    #Variables para el algoritmo
    path = ''
    num_clusters = 0
    num_iteraciones_totales = 100 #100 Iteraciones del algoritmo por defecto
    similitud_cluster = True
    criterios= ['Criterio de iteraciones', 'Criterio de similitud']
    criterio_de_parada= 1 #Por defecto esta activado el criterio de similitud --> 0 criterio de iteraciones
    iteraciones = 0 # 100 iteraciones por defecto

    #Menu de la interfaz
    menu = Menu(root)
    file = Menu(root,font=("Verdana", 9))
    file.add_command(label='Seleccionar archivo', command=openFile)
    file.add_command(label='Configuración', command=configuracion)
    file.add_command(label='Salir', command=root.destroy)
    menu.add_cascade(label='Menu', menu=file,font=("Verdana", 9))
    root.config(menu=menu)

    #Frame para el inicio de la interfaz
    inicio = Frame(root)
    label_inicio = Label(inicio, text="Variables del algoritmo")
    label_inicio.grid(row=0, column=0)
    label_inicio.config(font=('Verdana', 15))
    inicio.pack()

    #Listado de las variables para lanzar el algoritmo
    listbox = Listbox(root, font=("Verdana", 9), width=40, height= 8)
    listbox.pack()
    for item in ["Archivo: ", "Numero de clusters: ", "Iteraciones totales del algoritmo: ",
                 "Iteraciones por cluster : ", "Criterio de parada: "]:
        listbox.insert(END, item)

    #Frame para separar los botones del listado de variables
    botones = Frame(root)
    f_automatica = tk.Button(botones, font=("Verdana", 10), text="Algoritmo automatico").grid(row=0, column=0)
    f_manual = tk.Button(botones, font=("Verdana", 10), text="Algoritmo manual").grid(row=0, column=1)
    actualizar = tk.Button(botones, font=("Verdana", 10),  text="Actualizar", command=partial(actualizar, listbox)).grid(row=0, column=3)
    salir = Frame(root)
    cancelar = tk.Button(salir, font=("Verdana", 10), text="Salir",
                         command=root.destroy).grid(row=0, column=0)
    botones.pack()
    salir.pack()



root.mainloop()