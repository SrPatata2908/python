print ("Numero Negativo")
while True:
    try:
        numero = float(input("Pon un numero negativo: "))
        if numero < 0:
         break
    except ValueError:
        print("Introduzca un numero valido")
print("Tu numero negativo es:", numero,)