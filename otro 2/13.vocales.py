contador = 0
nombre = input("Dime tu nombre: ")
nombre.lower()
for letras in nombre:
    if (letras == "a" or letras == "e" or letras == "i" or letras == "o" or letras == "u"):
        contador +=1
print(f"Tu nombre {nombre} tiene {contador} vocales")