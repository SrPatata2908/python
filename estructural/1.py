monto = int(input("Ingresa el monto de tu compra: "))
descuento = 0 
if monto <= 500:
    descuento = 0
elif monto >= 1000 and monto <= 7000:
    descuento = 0.11
elif monto >= 7000 and monto <= 15000:
    descuento = 0.18
elif monto >= 15000:
    descuento = 0.25
elif monto >= 500 and monto <= 1000:
    descuento = 0.05
final = monto - (monto * descuento)
print (f"El monto de la compra fue de {monto}")
print (f"El descuento aplicado fue de {monto*descuento}")
print (f"El total a pagar es de {final}")