sueldo = int(input("Ingresa el sueldo del trabajador: "))
horaex = int(input("Ingresa tus horas extras trabajadas: "))
cate = int(input("Ingresa la categoria del trabajador: "))
match (cate):
    case 1 : phe = 30
    case 2: phe = 38
    case 3 : phe = 50
    case 4 : phe = 70
pagoex = phe * horaex
pagototal = sueldo + pagoex
print(f"Tus pagos extras son de {pagoex}$")
print(f"El pago total es de {pagototal}$")