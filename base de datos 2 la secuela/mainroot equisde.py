

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


conexion = mysql.connector.connect(host="localhost", user="root", password="", database="escuela")


def cargar_datos():
    tree.delete(*tree.get_children())  # Borrar datos existentes en el Treeview
    cursor = conexion.cursor()
    cursor.execute("select alumnos.nombre, alumnos.apellido, alumnos.dni, Carreras.nombre, estado_alumno.nombre from alumnos join carreras on alumnos.id_carrera = carreras.id_carrera join estado_alumno on estado_alumno.id_estado_alumno = alumnos.id_estado_alumno where alumnos.id_estado_alumno != 2")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)
    

def modificar_datos():
    
    dicc = tree.item(tree.selection())
    cambiar = dicc['values'][2]

    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    dni = dni_entry.get()
    carrera_nombre = carrera_combobox.get()
    estado_alumno = 1  # Valor predeterminado para IDESTADOALUMNO
    

    if nombre and apellido and dni and carrera_nombre:
        if (len(str(dni)) == 8) and (str(dni)).isnumeric():
            # Obtener el ID de la carrera seleccionada
            carreras = cargar_carreras()
            carrera_id = None
            for carrera in carreras:
                if carrera[1] == carrera_nombre:
                    carrera_id = carrera[0]
                    break

            cursor = conexion.cursor()
            # Insertar un nuevo registro en la tabla Alumnos con el ID de carrera y el valor predeterminado para IDESTADOALUMNO

            cursor.execute("""update alumnos set
                               nombre = %s,
                               apellido = %s,
                               dni = %s,
                               id_carrera = %s,
                               id_estado_alumno = %s
                               where dni = %s""", (nombre, apellido, dni, carrera_id, estado_alumno, cambiar))
            conexion.commit()
            cargar_datos()  # Actualizar la vista
            # Limpiar los campos después de insertar
            nombre_entry.delete(0, tk.END)
            apellido_entry.delete(0, tk.END)
            dni_entry.delete(0, tk.END)
            carrera_combobox.set("")  # Limpiar la selección del ComboBox
        else:
            mostrar_alerta("DNI no valido")
    else:
        mostrar_alerta("Los campos son obligatorios. Debe completarlos.")

    
    estado_alumno = 1  # Valor predeterminado para IDESTADOALUMNO
    cursor = conexion.cursor()
    
    conexion.commit()
    cargar_datos()  # Actualizar la vista
    # Limpiar los campos después de insertar
    nombre_entry.delete(0, tk.END)
    apellido_entry.delete(0, tk.END)
    dni_entry.delete(0, tk.END)
    carrera_combobox.set("")  # Limpiar la selección del ComboBox

# Función para obtener las carreras desde la base de datos y cargarlas en el ComboBox
def cargar_carreras():
    cursor = conexion.cursor()
    cursor.execute("select id_carrera, nombre from carreras order by nombre")
    carreras = cursor.fetchall()
    carrera_combobox['values'] = [row[1] for row in carreras]
    return carreras  # Devolver también la lista de carreras con sus IDs

# Función para mostrar una ventana de alerta
def mostrar_alerta(mensaje):
    messagebox.showwarning("Alerta", mensaje)

# Función para guardar un nuevo registro de alumno
def guardar_alumno():
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    dni = dni_entry.get()
    carrera_nombre = carrera_combobox.get()
    estado_alumno = 1  # Valor predeterminado para IDESTADOALUMNO
    

    if nombre and apellido and dni and carrera_nombre:
        if (len(str(dni)) == 8) and (str(dni)).isnumeric():
            # Obtener el ID de la carrera seleccionada
            carreras = cargar_carreras()
            carrera_id = None
            for carrera in carreras:
                if carrera[1] == carrera_nombre:
                    carrera_id = carrera[0]
                    break

            cursor = conexion.cursor()
            # Insertar un nuevo registro en la tabla Alumnos con el ID de carrera y el valor predeterminado para IDESTADOALUMNO

            cursor.execute("INSERT INTO alumnos (nombre, apellido, dni, id_carrera, id_estado_alumno) VALUES (%s, %s, %s, %s, %s)", (nombre, apellido, dni, carrera_id, estado_alumno))
            conexion.commit()
            cargar_datos()  # Actualizar la vista
            # Limpiar los campos después de insertar
            nombre_entry.delete(0, tk.END)
            apellido_entry.delete(0, tk.END)
            dni_entry.delete(0, tk.END)
            carrera_combobox.set("")  # Limpiar la selección del ComboBox
        else:
            mostrar_alerta("DNI no valido")
    else:
        mostrar_alerta("Los campos son obligatorios. Debe completarlos.")


root = tk.Tk()
root.title("Consulta de Alumnos")
root.resizable(0, 0)

# Crear un frame con un borde visible para el formulario de inscripción
formulario_frame = tk.Frame(root, bd=2, relief=tk.SOLID)
formulario_frame.grid(padx=10, pady=10)

# Título del formulario
titulo_label = tk.Label(formulario_frame, text="Formulario Inscripción", font=("Helvetica", 14))
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

# Campos de entrada para nombre, apellido y DNI con el mismo ancho que el ComboBox
nombre_label = tk.Label(formulario_frame, text="Nombre:")
nombre_label.grid(row=1, column=0)
nombre_entry = tk.Entry(formulario_frame)
nombre_entry.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

apellido_label = tk.Label(formulario_frame, text="Apellido:")
apellido_label.grid(row=2, column=0)
apellido_entry = tk.Entry(formulario_frame)
apellido_entry.grid(row=2, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

dni_label = tk.Label(formulario_frame, text="DNI:")
dni_label.grid(row=3, column=0)
dni_entry = tk.Entry(formulario_frame)
dni_entry.grid(row=3, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

# Combo box para la carrera
carrera_label = tk.Label(formulario_frame, text="Carrera:")
carrera_label.grid(row=4, column=0)
carrera_combobox = ttk.Combobox(formulario_frame,  state="readonly")# Configurar el ComboBox como de solo lectura
carrera_combobox.grid(row=4, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

# Cargar las carreras al inicio de la aplicación y obtener la lista de carreras con sus IDs
carreras = cargar_carreras()


guardar_button = tk.Button(formulario_frame, text="Guardar", command=guardar_alumno)
guardar_button.grid(row=5, columnspan=2, pady=10, sticky="ew")


tree = ttk.Treeview(root, columns=("Nombre", "Apellido","DNI", "Carrera","Estado Alumno"))
tree.heading("#1", text="Nombre")
tree.heading("#2", text="Apellido")
tree.heading("#3", text="DNI")
tree.heading("#4", text="Carrera")
tree.heading("#5", text="Estado Alumno")
tree.column("#0", width=0, stretch=tk.NO)

tree.column("#1", anchor=tk.CENTER)
tree.column("#2", anchor=tk.CENTER)
tree.column("#3", anchor=tk.CENTER)
tree.column("#4", anchor=tk.CENTER)
tree.column("#5", anchor=tk.CENTER) 
tree.column("#0", width=0, stretch=tk.NO)

tree.grid(row=6,padx=10, pady=10)


cargar_button = tk.Button(root, text="Cargar Datos", command=cargar_datos)
cargar_button.grid(row= 7, column= 0, padx=(0,120))

modificar_button = tk.Button(root, text="Modificar Datos", command=modificar_datos)
modificar_button.grid(row= 7, column= 0, padx=(120,0))


root.mainloop()
conexion.close()