

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


conexion = mysql.connector.connect(host="localhost", user="root", password="", database="escuela")


def cargar_datos():
    tree.delete(*tree.get_children())  # Borrar datos existentes en el Treeview
    cursor = conexion.cursor()
    cursor.execute("select alumnos.id_alumno, alumnos.nombre, alumnos.apellido, alumnos.dni, Carreras.nombre, estado_alumno.nombre from alumnos join carreras on alumnos.id_carrera = carreras.id_carrera join estado_alumno on estado_alumno.id_estado_alumno = alumnos.id_estado_alumno where alumnos.id_estado_alumno != 2 and alumnos.activo = 1")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)
    



##########################################################################################



def eliminar_alumno():
    id_eliminar = (    tree.item(tree.selection()) )['values'][0]

    result = messagebox.askquestion("Confirmar Eliminación", "¿Seguro desea eliminar este alumno?")
    
    if result == "yes":
        cursor = conexion.cursor()
        cursor.execute(f"update alumnos set activo = 0 where id_alumno = {id_eliminar}")
        conexion.commit()
        cargar_datos()

        
        
        








#######################################################################################3













def on_treeview_select(event):
    selected_item = tree.selection()
    
    if selected_item:
        modificar_button.config(state=tk.NORMAL)
        eliminar_button.config(state=tk.NORMAL)
        dicc = (    tree.item(tree.selection()) )['values']
        cambiar_id = dicc[0]

        nombre_entry.delete(0,"end") ; nombre_entry.insert(0,dicc[1])
        apellido_entry.delete(0,"end") ; apellido_entry.insert(0,dicc[2])
        dni_entry.delete(0,"end") ; dni_entry.insert(0,dicc[3])

        cursor = conexion.cursor()
        cursor.execute(f"select alumnos.id_carrera, alumnos.id_estado_alumno from alumnos where id_alumno = {cambiar_id};".format(cambiar_id))
        carrera_estado = cursor.fetchall()
        carrera = carrera_estado[0][0] ; estado = carrera_estado[0][1]
        carrera_combobox.current(carrera -1)
        estado_combobox.current(estado -1)
    else:
        modificar_button.config(state=tk.DISABLED)
        eliminar_button.config(state=tk.DISABLED)
    








# Función para obtener las carreras desde la base de datos y cargarlas en el ComboBox
def cargar_carreras():
    cursor = conexion.cursor()
    cursor.execute("select id_carrera, nombre from carreras order by nombre")
    carreras = cursor.fetchall()
    carrera_combobox['values'] = [row[1] for row in carreras]
    return carreras


def cargar_estados():
    cursor = conexion.cursor()
    cursor.execute("select id_estado_alumno, nombre from estado_alumno")
    estados = cursor.fetchall()
    estado_combobox['values'] = [row[1] for row in estados]
    return estados






def mostrar_alerta(mensaje):
    messagebox.showwarning("Alerta", mensaje)





##############################################################################################################




# Función para guardar un nuevo registro de alumno
def guardar_alumno(parametro):
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    dni = dni_entry.get()
    carrera_nombre = carrera_combobox.get()
    estado_nombre = estado_combobox.get()
    

    if nombre and apellido and dni and carrera_nombre and estado_nombre:
        if (len(str(dni)) == 8) and (str(dni)).isnumeric():
            # Obtener el ID de la carrera seleccionada
            carreras = cargar_carreras()
            carrera_id = None
            for carrera in carreras:
                if carrera[1] == carrera_nombre:
                    carrera_id = carrera[0]
                    break

            estados = cargar_estados()
            estado_id = None
            for estado in estados:
                if estado[1] == estado_nombre:
                    estado_id = estado[0]
                    break

            cursor = conexion.cursor()
            # Insertar un nuevo registro en la tabla Alumnos con el ID de carrera y el valor predeterminado para IDESTADOALUMNO
            if parametro == 0:
                cursor.execute("INSERT INTO alumnos (nombre, apellido, dni, id_carrera, id_estado_alumno, activo) VALUES (%s, %s, %s, %s, %s, %s)", (nombre, apellido, dni, carrera_id, estado_id, 1))
            else:
                dicc = (    tree.item(tree.selection()) )['values']
                cambiar_id = dicc[0]
                cursor.execute("update alumnos set nombre = %s, apellido = %s, dni = %s, id_carrera = %s, id_estado_alumno = %s where id_alumno = %s", (nombre, apellido, dni, carrera_id, estado_id,cambiar_id))
            conexion.commit()
            cargar_datos()  # Actualizar la vista
            # Limpiar los campos después de insertar
            nombre_entry.delete(0, tk.END)
            apellido_entry.delete(0, tk.END)
            dni_entry.delete(0, tk.END)
            carrera_combobox.set("")  # Limpiar la selección del ComboBox
            estado_combobox.set("")
        else:
            mostrar_alerta("DNI no valido")
    else:
        mostrar_alerta("Los campos son obligatorios. Debe completarlos.")







##############################################################################################################





root = tk.Tk()
root.title("Consulta de Alumnos")
root.resizable(0, 0)


formulario_frame = tk.Frame(root, bd=2, relief=tk.SOLID)
formulario_frame.grid(padx=10, pady=10)

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
carrera_combobox = ttk.Combobox(formulario_frame,  state="readonly")
carrera_combobox.grid(row=4, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

# Combo box para el estado
estado_label = tk.Label(formulario_frame, text="Estado:")
estado_label.grid(row=5, column=0)
estado_combobox = ttk.Combobox(formulario_frame,  state="readonly")
estado_combobox.grid(row=5, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")





# Cargar las carreras al inicio de la aplicación y obtener la lista de carreras con sus IDs
carreras = cargar_carreras()
estados = cargar_estados()


guardar_button = tk.Button(formulario_frame, text="Guardar", command= lambda : guardar_alumno(0))
guardar_button.grid(row=6, columnspan=2, pady=10, sticky="ew")


tree = ttk.Treeview(root, columns=("Codigo","Nombre", "Apellido","DNI", "Carrera","Estado Alumno"))
tree.bind("<<TreeviewSelect>>",on_treeview_select)

tree.heading("#1", text="Codigo")
tree.heading("#2", text="Nombre")
tree.heading("#3", text="Apellido")
tree.heading("#4", text="DNI")
tree.heading("#5", text="Carrera")
tree.heading("#6", text="Estado Alumno")


tree.column("#0", width=0, stretch=tk.NO)
tree.column("#1", width=0, stretch=tk.NO)
tree.column("#2", anchor=tk.CENTER)
tree.column("#3", anchor=tk.CENTER)
tree.column("#4", anchor=tk.CENTER)
tree.column("#5", anchor=tk.CENTER)
tree.column("#6", anchor=tk.CENTER) 


tree.grid(row=7,padx=10, pady=10)


cargar_button = tk.Button(root, text="Cargar Datos", command=cargar_datos)
cargar_button.grid(row= 8, column= 0, padx=(0,200))

modificar_button = tk.Button(root, text="Modificar Datos",state="disabled", command= lambda : guardar_alumno(1))
modificar_button.grid(row= 8, column= 0, padx=(0,0))

eliminar_button = tk.Button(root, text="Eliminar Alumno",state="disabled", command= eliminar_alumno)
eliminar_button.grid(row= 8, column= 0, padx=(220,0))


root.mainloop()
conexion.close()