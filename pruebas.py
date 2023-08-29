mi_respuesta = ['0', '605']
respuesta_correcta = ['0', '605633802']



condicion2 = True
for i in range(len(mi_respuesta[1])):
    if mi_respuesta[1][i] != respuesta_correcta[1][i]:
        condicion2 = False

if condicion2 == True:
    print("ALELUYA")