
def si_o_no(txt):
    flag = True
    while flag == True:
        op = input(txt)

        op = op.lower()

        if (op == "1") or (op == "si"):
            answer = 1
            flag = False
        elif (op == "2") or (op == "no"):
            answer = 2
            flag = False
        else:
            print("opcion ingresada no es valida")
    
    return answer

op = si_o_no("1) SI         2) NO")

print(op)