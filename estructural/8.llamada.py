tiempo = int(input("Dime cuantos minutos duro tu llamada: "))
print ("Estas son las claves de cada pais")
print ("12 DE A.N")
print ("15 DE A.C")
print ("18 DE A.S")
print ("19 DE EUROPA")
print ("23 DE ASIA")
print ("25 DE AFRICA")
print ("29 DE OCEANIA")
clave = int(input("Ingresa la clave de la zona de tu llamada: "))
match (clave):
    case 12 : precio = 2
    case 15 : precio = 2.2
    case 18 : precio = 4.5
    case 19 : precio = 3.5
    case 23 : precio = 6
    case 12 : precio = 6
    case 12 : precio = 5
costo = precio * tiempo
print(f"El costo de la llamada fue de {costo}")