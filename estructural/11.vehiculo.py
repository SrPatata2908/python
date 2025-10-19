monto = int(input("Cual es el monto total del vehiculo: "))
enganche = monto * 0.35
resto = monto - enganche
menso = resto / 18
print(f"El enganche a pagar es de {enganche: ,}$")
print(f"Y la mensualidad por 18 meses quedaria de {menso: .2f}$")
#ecuacion de