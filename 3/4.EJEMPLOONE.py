class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
  
    def mostrar_datos (self):
        print(f"Nombre: {self.nombre}")
        print(f"edad: {self.edad}")

mi_persona = Persona ("Ana", 30)
alan_moreno = Persona ("Alan", 40)
print(f"Me llamo {mi_persona.nombre} y tengo {mi_persona.edad} años")
print(f"Me llamo {alan_moreno.nombre} y tengo {alan_moreno.edad} años")