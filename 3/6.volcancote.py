import math
class volcan:
    def __init__(self, nombre, altura, diametro):
        self.nombre = nombre
        self.altura = altura
        self.diametro = diametro

    def calcular_volumen (self):
        radmetr = (self.diametro * 1000) / 2
        volumen_metro = (1/3) * math.pi * (radmetr ** 2) * self.altura
        return volumen_metro
    
mi_volca = volcan("Popocatepet", 5426, 25)
print(f"El volcan se llama {mi_volca.nombre}")
print(f"Su altura es de {mi_volca.altura} m")
print(f"Su diametro es de {mi_volca.diametro} km")
print(f"El volumen aproximado es de {mi_volca.calcular_volumen(): ,.2f} metros cubicos")