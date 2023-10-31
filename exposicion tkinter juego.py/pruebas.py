from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk  # Importa Image y ImageTk desde PIL

from funciones import *

root = Tk()
root.resizable(0, 0)
root.attributes("-fullscreen", True)

window_frame = Frame(root)
window_frame.place(x=0, y=0)

minimizar_button = ttk.Button(window_frame, text="[ - ]", command=lambda: minimisar_juego(root))
minimizar_button.pack(side=LEFT, anchor=N)

exit_button = ttk.Button(window_frame, text="X", command=lambda: salir_del_juego(root))
exit_button.pack(side=LEFT, anchor=N)

# Abre la imagen y redimensiona antes de convertirla en PhotoImage
isaui_imagen = Image.open("ISAUI 40.png")
isaui_imagen = isaui_imagen.resize((300, 205), Image.ANTIALIAS)
isaui_icono = ImageTk.PhotoImage(isaui_imagen)

label = ttk.Label(image=isaui_icono)
label.pack()

encuesta(root, 0)

root.mainloop()