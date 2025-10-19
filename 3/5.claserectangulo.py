class rectangulo:
    def __init__ (self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    def calcular_area (self):
        ar = self.alto * self.ancho
        return ar
    def calcular_perimetro (self):
        peri = 2 * (self.alto + self.ancho)
        return peri
mi_rectangulo = rectangulo(10, 5)
print(f"El area del rectangulo {mi_rectangulo.calcular_area()}")
print(f"El perimetro del rectangulo es: {mi_rectangulo.calcular_perimetro()}")