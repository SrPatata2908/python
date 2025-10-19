print("Calculador de 5 Calificaciones del semestre.")
cincoprome = 0 
for i in range(5):
    califi = float(input(f"Ingrese la calificacion #{i + 1}: "))
    cincoprome += califi
promed = cincoprome / 5
print(F"El promedio de las 5 calificaciones es: {promed}")