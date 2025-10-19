class coche:
    def __init__(self, color, velocidad):
        self.color = color
        self.velocidad = velocidad
    def acelerar (self, aumento):
        self.velocidad += aumento
        
    def frenar (self, disminucion):
        self.velocidad -= disminucion

#crear el coche
mi_coche = coche ("rojo", 0)
mi_coche.acelerar (50)

print(f"Color del coche: {mi_coche.color}")
print(f"Velocidad actual: {mi_coche.velocidad}")
mi_coche.frenar (30)

print(f"Color del coche: {mi_coche.color}")
print(f"Velocidad actual: {mi_coche.velocidad}")
mi_coche.acelerar (50)

print(f"Color del coche: {mi_coche.color}")
print(f"Velocidad actual: {mi_coche.velocidad}")