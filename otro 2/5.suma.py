try:
    multiplicando = int(input("Ingresa tu primer numero: "))
    multiplicador = int(input("Ingresa tu segundo numero: "))
    if multiplicador < 0: 
        print("El multiplicador debe ser un numero positivo")
    else:
       resultado = 0 
       for _ in range(multiplicador):
           resultado += multiplicando
           print (f"El resultado es igual a {resultado}")
except ValueError:
    print("Entrada inválida. Por favor, ingresa solo números enteros.")