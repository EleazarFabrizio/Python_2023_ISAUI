from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image as Imaggen


import sqlite3

import random
import time

base_de_datos = sqlite3.connect("Base_de_datos.bd")

mycursor = base_de_datos.cursor()

global datos_usuario
#/ Nombre / Instagram / Puntaje / tiempo / puntaje_total
datos_usuario = []

global aciertos
global tiempo
aciertos = 0
tiempo = 0




##################
# WINDOW BUTTONS #
##################


def minimisar_juego(root):
    if root.attributes()[7] == 1:
        root.attributes("-fullscreen", False)
    else:
        root.attributes("-fullscreen", True)
def salir_del_juego(root):
    root.destroy()

###################
# MOSTRAR ALERTAS #
###################

def mostrar_alerta(mensaje):
    messagebox.showwarning("Alerta", mensaje)


def encuesta(root,frame_anterior):

    

    #####################################################
    # CONTROL DE FORGET. 0 SIGNIFICA QUE VIENE DEL MENU #
    #####################################################

    if frame_anterior != 0:
        frame_anterior.destroy()

        

    global aciertos
    aciertos = 0
    global tiempo
    tiempo = 0
    global datos_usuario
    datos_usuario = []


    #########################################################
    # LAS PREGUNTAS DE VUELVEN RANDOM Y SE CREA LA ENCUESTA #
    #########################################################


    preguntas_desorganizadas = al_azar()

    marco_encuesta = Frame(root)

    marco_encuesta.pack(pady=(50,0))


    #########################
    # LIMITANDO LOS ENTRIES #
    #########################

    

    jugar_button = Button(marco_encuesta,text="JUGAR",font=("Velvetica", 25),command= lambda : jugar(root,marco_encuesta,0,preguntas_desorganizadas,''))
    jugar_button.grid(row=2,columnspan=3,pady=(75,50))

    

    ##############
    # SCOREBOARD #
    ##############

    score_board = ttk.Treeview(marco_encuesta, columns=("Codigo","Nombre","Instagram","Aciertos", "Tiempo", "Puntaje Total"),height=15)

    score_board.heading("#1", text="Codigo")
    score_board.heading("#2", text="Nombre")
    score_board.heading("#3", text="Instagram")
    score_board.heading("#4", text="Aciertos")
    score_board.heading("#5", text="Tiempo")
    score_board.heading("#6", text="Puntaje Total")


    score_board.column("#0", width=0, stretch=tk.NO)
    score_board.column("#1", width=0, stretch=tk.NO)
    score_board.column("#2", anchor=tk.CENTER,width=300)
    score_board.column("#3", anchor=tk.CENTER,width=300)
    score_board.column("#4", anchor=tk.CENTER,width=300)
    score_board.column("#5", anchor=tk.CENTER,width=300)
    score_board.column("#6", anchor=tk.CENTER,width=300)

    score_board.grid(row=3,columnspan=3)

    score_board.delete(*score_board.get_children())  # Borrar datos existentes en el Treeview
    mycursor.execute("select id_usuario, nombre, instagram, aciertos, tiempo, puntaje_total from usuario order by puntaje_total DESC")
    for row in mycursor.fetchall():
        score_board.insert("", "end", values=row)

    



###################################################################################################
# PREGUNTA NUMERO ES EL NUMERO DE UNA DE LAS 16 RONDAS. PREGUNTAS ES LA LISTA DE PREGUNTAS RANDOM #
###################################################################################################

def jugar(root,frame_anterior,pregunta_numero,preguntas,respuesta_anterior):


        global aciertos

        #print(respuesta_anterior)

        #print(preguntas[pregunta_numero-1][2])


        if respuesta_anterior != '':
            if (respuesta_anterior == preguntas[pregunta_numero - 1][2]):
                aciertos += 1

        frame_anterior.destroy()

        marco_juego = Frame(root)
        marco_juego.pack(pady=(50,0))

        if pregunta_numero == 16:
            en_hora_buena(root,marco_juego)
        
        else:
            next_pregunta = pregunta_numero + 1

            respuestas = [preguntas[pregunta_numero][random.randint(2,5)]]
            con = 0
            while con < 3:
                numero_random = random.randint(2,5)
                repetido = False
                for k in range(0,len(respuestas)):
                    if preguntas[pregunta_numero][numero_random] == respuestas[k]:
                        repetido = True
                if repetido == False:
                    respuestas.append(preguntas[pregunta_numero][numero_random])
                    con += 1


            pregunta_label = ttk.Label(marco_juego,text=preguntas[pregunta_numero][1],font=("Velvetica", 40))
            pregunta_label.grid(row=0,column=0,pady=(50,50))

            respuesta_1_button = Button(marco_juego,text=respuestas[0],font=("Velvetica", 25),command= lambda : jugar(root,marco_juego,next_pregunta,preguntas,respuesta_1_button['text']), width=90,fg="white", bg="#005ad9",height=2)
            respuesta_1_button.grid(row=1,column=0,padx=100,pady=50)

            respuesta_2_button = Button(marco_juego,text=respuestas[1],font=("Velvetica", 25),command= lambda : jugar(root,marco_juego,next_pregunta,preguntas,respuesta_2_button['text']), width=90,fg="white", bg="#005ad9",height=2)
            respuesta_2_button.grid(row=2,column=0,padx=100,pady=50)

            respuesta_3_button = Button(marco_juego,text=respuestas[2],font=("Velvetica", 25),command= lambda : jugar(root,marco_juego,next_pregunta,preguntas,respuesta_3_button['text']), width=90,fg="white", bg="#005ad9",height=2)
            respuesta_3_button.grid(row=3,column=0,padx=100,pady=50)

            respuesta_4_button = Button(marco_juego,text=respuestas[3],font=("Velvetica", 25),command= lambda : jugar(root,marco_juego,next_pregunta,preguntas,respuesta_4_button['text']), width=90,fg="white", bg="#005ad9",height=2)
            respuesta_4_button.grid(row=4,column=0,padx=100,pady=50)

def mostrar_preguntas():
    res = base_de_datos.execute("SELECT * from pregunta")

    data = res.fetchall()
    return data



def al_azar():

    data = mostrar_preguntas()

    con = 0
    preguntas_desorganizadas = [data[random.randint(0,15)]]
    while con < 15:
        lugar_pregunta = random.randint(0,15)
        repetido = False
        for k in range(0,len(preguntas_desorganizadas)):
            if data[lugar_pregunta][0] == preguntas_desorganizadas[k][0]:
                repetido = True
        if repetido == False:
            preguntas_desorganizadas.append(data[lugar_pregunta])
            con += 1

    return(preguntas_desorganizadas)
    #print(data)
    #for row in desorganizado:
    #    print(row)






def en_hora_buena(root,frame_anterior):

    frame_anterior.destroy()
    
    ### FINALIZA CRONOMETRO

    tiempo_transcurrido = (time.time() - tiempo) * 1000

    minutos, segundos = divmod(tiempo_transcurrido / 1000, 60)
    segundos, milisegundos = divmod(segundos, 1)

    tiempo_total = f"{int(minutos)} m : {int(segundos)} s : {int(milisegundos * 1000)} ms"


    puntaje_total = aciertos*100 - round(tiempo_transcurrido/500 , 2)

    #########################

    datos_usuario.append(aciertos)

    datos_usuario.append(tiempo_total)

    datos_usuario.append(puntaje_total)
    

    #########################

    marco_party = Frame(root)

    marco_party.pack(pady=(50,0))

    felicidades_label = ttk.Label(marco_party,text="Felicidades!",font=("Velvetica", 50))
    felicidades_label.pack()

    felicidades2_label = ttk.Label(marco_party,text="Respuestas Correctas :",font=("Velvetica", 25))
    felicidades2_label.pack()

    puntaje_label = ttk.Label(marco_party,text=f"{aciertos}",font=("Velvetica 90 bold"),foreground="#005ad9")
    puntaje_label.pack()

    felicidades3_label = ttk.Label(marco_party,text="Tiempo Logrado :",font=("Velvetica", 25))
    felicidades3_label.pack()

    tiempo_label = ttk.Label(marco_party,text=f"{tiempo_total}",font=("Velvetica 60 bold"),foreground="#005ad9")
    tiempo_label.pack()

    puntaje_total_label = ttk.Label(marco_party,text="Puntaje Total :",font=("Velvetica", 40))
    puntaje_total_label.pack()

    puntaje_total_label2 = ttk.Label(marco_party,text=f"{puntaje_total}",font=("Velvetica 90 bold"),foreground="#005ad9")
    puntaje_total_label2.pack()

    regresar_button = Button(marco_party,text="Regresar",font=("Velvetica", 25),command= lambda: encuesta(root,marco_party))
    regresar_button.pack(pady=(75,50))

    mycursor.execute("INSERT INTO Usuario (nombre, instagram, aciertos, tiempo, puntaje_total) VALUES (?, ?, ?, ?, ?)", (datos_usuario[0],datos_usuario[1],datos_usuario[2],datos_usuario[3],datos_usuario[4]))

    base_de_datos.commit()

