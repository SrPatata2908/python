print("Encontrar Multiplos de 3")
primer = int(input("Ingresa de que numero quieres empezar: "))
segundo = int(input("Ingresa el numero al donde quieres acabar: "))
for numero in range (primer, segundo):
    if numero %3 == 0:
        print(f"Los numeros multiplos son: {numero}")