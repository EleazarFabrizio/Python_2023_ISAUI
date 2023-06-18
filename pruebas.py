

msj = ""
for i in dicc:
    msj = msj + str(i)
    for k in dicc[i]:
        msj = msj + str(k) + "\n"

print (msj)