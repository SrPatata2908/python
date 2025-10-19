print ("Resolvedor de ecuacionn de 2°")
x = float(input("Coloca el primer valor de tu ecuacion: "))
y = float(input("Coloca el segundo valor de tu ecuacion: "))
r = float(input("Coloca el resultado de tu ecuacion: "))
xd = float(input("Coloca el primer valor de tu segunda ecuacion: "))
yd = float(input("Coloca el segundo valor de tu segunda ecuacion: "))
rd = float(input("Coloca el resultado de tu segunda ecuacion: "))
det = (x*yd)-(xd*y)
if det != 0:
    rx = ((r*yd)-(rd*y))/det 
    ry = ((x*rd)-(xd*r))/det
    rxredo = round(rx, 2)
    ryredo = round(ry, 2)
    print("El valor de X es:", rxredo ,"Y el valor de Y es:", ryredo)
else:
    print("no hay una sola solucion")