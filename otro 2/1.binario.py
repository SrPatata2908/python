deci = int(input("Escribe tu numero: "))
bina  = ""

while deci > 0:
    resi = deci % 2

    bina = str(resi) + bina

    deci = deci//2
    
print(f"El número binario es: {bina}")