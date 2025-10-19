#Semaforo
color = input("Color del semafoto: ")
if color.lower () == "rojo":
    print("Detenerse")
elif color.lower () == "amarillo":
    print("Precaucion")
elif color.lower () == "verde":
    print("Avanze")
else:
    print("Color no valido")