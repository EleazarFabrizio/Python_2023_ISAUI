from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image as Imaggen

from funciones import *


root = Tk()

root.resizable(0,0)

root.attributes("-fullscreen", True)

window_frame = Frame(root)
window_frame.place(x=0,y=0)

minimizar_button = ttk.Button(window_frame,text="[ - ]",command= lambda : minimisar_juego(root))
minimizar_button.pack(side=LEFT,anchor=N)

exit_button = ttk.Button(window_frame,text="X",command= lambda : salir_del_juego(root))
exit_button.pack(side=LEFT,anchor=N)



encuesta(root,0)



root.mainloop()