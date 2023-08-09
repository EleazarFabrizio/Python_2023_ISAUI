
def verificar(txt):

    try:

        if "/" in txt:
            txt = txt.replace("/" , " ")
            txt = txt.split()
            txt = float(txt[0]) / float(txt[1])

        elif "." in txt:
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