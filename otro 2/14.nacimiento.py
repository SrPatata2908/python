año = int(input("Ingresa tu año de nacimiento: "))
mes = int(input("Ingresa tu mes de nacimiento: "))
dia = int(input("Ingresa tu dia de nacimiento: "))
edad = 2025 - año
if (9, 3) < (mes, dia):
    edad -= 1
meses = 9 - mes
if meses < 0: 
    meses += 12
print(f"Tienes {edad} años y {meses} meses.")