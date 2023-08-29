
def verificar(txt):

    try:

        if "/" in txt:
            txt = txt.replace("/" , " ")
            txt = txt.split()
            txt = float(txt[0]) / float(txt[1])

        elif ("." in txt) or ("," in txt):
            txt = txt.replace("," , ".")
            txt2 = txt
            txt = float(txt)
            txt2 = txt2.replace("." , " ")
            txt2 = txt2.split()
            if int(txt2[1]) == 0:
                txt = int(txt2[0])

        else:
            txt = int(txt)

    except ValueError:
        txt = "error"

    return txt
    

def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    return a / b

def potenciar(a,b):
    return a ** b

def radicar(a,b):
    return a ** (1 / b)

def arreglar(num):
    x = num
    if "." in str(x):
        separado = str(x)
        separado = separado.replace("." , " ")
        separado = separado.split()
        if int(separado[1]) == 0:
            x = int(separado[0])
        
        else:
            periodo = ""
            anterior = []
            for i in separado[1]:
                if i in anterior:
                    return( float(separado[0] + "." + periodo))
                else:
                    periodo += i
                    anterior.append(i)
            x = float(separado[0] + "." + periodo)

    return x



def not_in(buscar,lista):
    for i in lista:
        for k in buscar:
            if k == i:
                return True
    return False


print(arreglar(2.260869565217391))
