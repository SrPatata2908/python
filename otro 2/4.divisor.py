try:
    dividiendo = int(input("Ingresa el dividiendo: "))
    divisor = int(input("Ingresa el divisor: "))

    if divisor == 0:
        print("Nose puede dividir por 0")
    else:
        cociente = 0 
        dviabd = abs(dividiendo)
        visoadb =abs(divisor)

        while dviabd >= visoadb:
            dviabd -= visoadb
            cociente += 1

        if (dividiendo < 0 and divisor > 0) or (dividiendo > 0 and divisor <0):
            cociente = -cociente
            resi = dividiendo - (cociente * divisor)

        print(f"El cociente de la división es: {cociente}")
        print(f"El residuo de la división es: {resi}")
except ValueError:
    print("Entrada inválida. Por favor, ingresa solo números enteros.")