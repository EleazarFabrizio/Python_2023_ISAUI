
x2=["12","333"]

per  = ""
ant = ""
for i in x2[1]:
    if ant == i:
        xx = ( x2[0] + "." + per )
    else:
        per += i
        ant = i

xx = ( x2[0] + "." + per )
print(xx)