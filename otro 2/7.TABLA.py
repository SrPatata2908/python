impresion = [""] * 11
for numero in range(1, 6):
        for multiplicador in range(1, 11):
            resultado = numero * multiplicador
            linea = f"{numero}x{multiplicador}={resultado}"
            impresion[multiplicador - 1] += f"{linea:<11}"
for fila in impresion:
       print(fila)
impresion = [""] * 11
for numero in range(6, 11):
        for multiplicador in range(1, 11):
            resultado = numero * multiplicador
            linea = f"{numero}x{multiplicador}={resultado}"
            impresion[multiplicador - 1] += f"{linea:<11}"
for fila in impresion:
       print(fila)