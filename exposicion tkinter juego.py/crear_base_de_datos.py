import sqlite3

base_datos = sqlite3.connect("Base_de_datos.bd")



base_datos.execute('''create table if not exists Usuario (
                 Id_usuario integer primary key autoincrement,
                 nombre varchar(255) not null,
                 instagram varchar(255) not null,
                 aciertos int not null,
                 tiempo varchar(255) not null,
                 puntaje_total double (255,2) not null
                 )''')

base_datos.execute('''create table if not exists pregunta (
                 id_pregunta integer primary key autoincrement,
                 texto varchar(255) not null,
                 respuesta varchar(255) not null,
                 falso varchar(255) not null,
                 falso_dos varchar(255) not null,
                 falso_tres varchar(255) not null
                )''')


pre_res =[
    ["¿En qué año se fundó?"    ,   "1983"  ,   "1982",     "2014"    ,    "1883"],
    ["¿Cuál fue el nombre del establecimiento educativo cuando se fundó? "," Complejo Facultativo De Enseñanza Superior San Francisco de Asís."   ,   "Instituto Superior de San Francisco de Asís."  ,   "Complejo Facultativo De Enseñanza Interdimencional San Antonio de Asís."    ,   "Escuela Para Super Dotados de Peguajo."],
    ["Cantidad de fundadores: ","16","34","29","12"],
    ["¿En qué año se convierte a colegio Nacional? "    ,   " 22/07/85 "   ,   " 25/09/58 "  ,   " 24/07/98 "  ,   " 12/08/85 "],
    ["¿Cuántos directores tuvo el Instituto hasta la fecha? "   ,  " Adolfo Bur, Mario Carletti, Gisela Flores, Maximiliano Ibañez."    ,   " Mario Brothers, Gasela Flores , minimiliano Albañil."  ,   " Mario Carletti, Justin Powers, Maximiliano Ibañez, Donatelo de las tortugas ninja adolescente mutantes."  ,   " Adolfo Bur, Gisela Judini."],
    ["¿Cuántas carreras se dictan actualmente en el ISAUI?","6" ,   "7" ,   "8" ,   "5"],
    ["¿Cuál fue el primer número de teléfono del Instituto?","41164"    ,   "41264"      ,        "61244"       ,      "51144"],
    ["¿Qué es el workshop? "," Una muestra a fin de año, donde los alumnos muestran sus trabajos."  ,       "Una muestra a principio de año, donde los alumnos muestran sus pasos de baile."      ,       "Una juntada entre amigos."     ,       "Donde le instalo mods a mis juegos de Steam."],
    ["¿Qué carrera fue la pionera con los viajes en las materias de prácticas?","Guía de turismo",        "Trekking"      ,       "Submarinismo"        ,       "Guía de Hostelería"],
    ["¿Cómo era el edificio educativo en sus comienzos?","Una casa con 3 ambientes"     ,       "Un living con una hermosa chimenea"        ,       "Un edificio bien equipado."     ,       "Dos edificios, tres aulas y un galpon."],
    ["¿ISAUI es un Instituto público?","Sí","No","Tal vez","¿Quien escribe estas preguntas?"],
    ["¿A partir de que año se empezaron a construir las aulas?","A partir de 1986. Una por año",        "A partir de 1987. El año en el que se situa fnaf",     "A partir de 1969. Una por año.",        "A partir de 1986. dos por año."],
    ["¿De donde provino el dinero para construir las aulas?","De la contribución de los padres."    ,   "Del programa espacial de Menem",       "Fraude fiscal",        "Un bono de Alberto Fernandez."],
    ["¿Quien fue presidente de la cooperativa durante los primeros años?","El SR.GATICA, luego el SR.CONSTANTE BOGADO.",        "El SR.GOTICA, luego el SR.CONSTIPADO ABOGADO.",        "El SR.LUIS, luego el SR.CONSTANTE BOGOTA.",        "La SRA.GATICA, luego la SRA.CONSTANTE BOGADA."],
    ["¿Quien es presidenta de la cooperativa actualmente?"  ,   "Daniela Maschio"   ,   "Carla Aliguieri"   ,   "Nicolas del Caño"  ,   "numero 5 de los chicos del barrio"],
    ["¿Como se logro la nacionalización?"     ,     "Mediante la gestión del diputado de Anselmo Pelaez."     ,     "Mediante la gestion del diputado Marcelo Nuñez."    ,     "Gracias a la presidencia de Menem."  ,   "Debido a la Convención de Vienna sobre el Derecho de los Tratados."]
]


for i in range(0,16):
    base_datos.execute('''insert into pregunta (texto,respuesta,falso,falso_dos,falso_tres) values (?,?,?,?,?)''', (pre_res[i][0] , pre_res[i][1] ,  pre_res[i][2] ,  pre_res[i][3],  pre_res[i][4]) )

base_datos.commit()


def mostrar_preguntas():
    res = base_datos.execute("SELECT * from pregunta")

    data = res.fetchall()

    for row in data:
        print(row)
    return data

base_datos.close()
#mostrar_preguntas()

