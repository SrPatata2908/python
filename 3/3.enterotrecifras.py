
while True:
    try:
        num_menor = int(input("Ingresa el número MENOR: "))
        num_mayor = int(input("Ingresa el número MAYOR: "))
        if num_menor <= num_mayor:
            break 
        else:
            print("Error")
    finally:
        print() 
print(f"Conteo de cifras para los números de {num_menor} a {num_mayor}:")

for numero in range(num_menor, num_mayor + 1):
    cantidad_cifras = len(str(abs(numero)))
    print(f"El número {numero} tiene {cantidad_cifras} cifra(s).")