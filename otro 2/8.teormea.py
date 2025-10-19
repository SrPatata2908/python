print("Teorema de Pitágoras")
print("escribe h =hipotenusa o c = cateto a lo que ocupes")
lado = input("¿Qué lado quieres calcular?): ")

if lado == "h":
    catea = float(input("Ingresa el primer cateto: "))
    cateb = float(input("Ingresa el segundo cateto: "))
    res = (catea**2 + cateb**2)
    print(f"La hipotenusa es: {res}")
elif lado == "c":
    hipotenusa = float(input("Ingresa la longitud: "))
    catexd = float(input("Ingresa el cateto: "))
    res = (hipotenusa**2 - catexd**2)
    print(f"el cateto es: {res}")
else:
    print("No valido.")