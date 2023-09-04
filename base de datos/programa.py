from tkinter import *
from tkinter import ttk
import mysql.connector



conexion = mysql.connector.connect(host="localhost",user="root",password="",database="almacen")

# Función para cargar y mostrar información en el Treeview

def cargar_datos():
    tree.delete(*tree.get_children()) # Borrar datos existentes en el Treeview
    cursor = conexion.cursor()
    cursor.execute("select producto.nombre, producto.precio, marca.nombre, categoria.nombre, producto.stock from producto join marca on marca.codmarca = producto.codmarca join categoria on categoria.codcategoria = producto.codcategoria")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)


root = Tk()
root.title("Consultar base de datos de almacen fantabuloso :P")

# Crear Treeview para mostrar la información
tree = ttk.Treeview(root, columns=("Nombre", "Precio", "Stock", "Marca","Categoria"))
tree.heading("#1", text="Nombre")
tree.heading("#2", text="Precio")
tree.heading("#3", text="Stock")
tree.heading("#4", text="Marca")
tree.heading("#5", text="Categoria")

tree.column("#0", width=0, stretch=NO)
tree.column("Nombre", anchor=CENTER)
tree.column("Precio", anchor=CENTER)
tree.column("Marca", anchor=CENTER)
tree.column("Categoria", anchor=CENTER)
tree.column("Stock", anchor=CENTER)
tree.pack(padx=10, pady=10)


cargar_button = ttk.Button(root, text="Cargar Datos", command=cargar_datos)
cargar_button.pack(pady=5)


root.mainloop()
conexion.close()