import math

class figuritas:
    def __init__(self, fig, r=None, l1=None, l2=None, l3=None, b=None, h=None, medida=None, nolados=None, ap=None):
        self.fig = fig
        self.r = r
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.b = b
        self.h = h
        self.medida = medida
        self.nolados = nolados
        self.ap = ap

    def circulo(self, opc):
        if opc == "a":
            return math.pi * self.r**2
        elif opc == "p":
            return 2 * math.pi * self.r
        return 0

    def triangulo(self, opc):
        if opc == "p":
            return self.l1 + self.l2 + self.l3
        elif opc == "a":
            return (self.b * self.h) / 2
        return 0

    def rectangulo(self, opc):
        if opc == "a":
            return self.b * self.h
        elif opc == "p":
            return 2 * (self.b + self.h)
        return 0

    def poligono(self, opc):
        perimetro = self.medida * self.nolados
        if opc == "a":
            return (perimetro * self.ap) / 2
        elif opc == "p":
            return perimetro
        return 0

# --- Menú Principal ---
opcion = ""
while opcion != "5":
    print("      MENÚ DE CÁLCULO DE FIGURITAS       ")
    print("1. Círculo")
    print("2. Triángulo")
    print("3. Rectángulo")
    print("4. Polígono Regular")
    print("5. Salir")
    opcion = input("Elige la figura que quieres calcular (1-5): ")
    print()

    try:
        if opcion == "1":
            # --- Pedir datos para el Círculo ---
            radio = float(input("Ingresa el radio del círculo: "))
            figura = figuritas(fig=1, r=radio)
            calculo = input("¿Qué quieres calcular? (a para área, p para perímetro): ").lower()
            resultado = figura.circulo(opc=calculo)
            print(f"El resultado es: {resultado:.2f}\n")

        elif opcion == "2":
            # --- Pedir datos para el Triángulo ---
            print("Para el área:")
            base = float(input("  Ingresa la base: "))
            altura = float(input("  Ingresa la altura: "))
            print("Para el perímetro:")
            lado1 = float(input("  Ingresa el lado 1: "))
            lado2 = float(input("  Ingresa el lado 2: "))
            lado3 = float(input("  Ingresa el lado 3: "))
            figura = figuritas(fig=2, l1=lado1, l2=lado2, l3=lado3, b=base, h=altura)
            calculo = input("¿Qué quieres calcular? (a para área, p para perímetro): ").lower()
            resultado = figura.triangulo(opc=calculo)
            print(f"El resultado es: {resultado:.2f}\n")

        elif opcion == "3":
            # --- Pedir datos para el Rectángulo ---
            base = float(input("Ingresa la base del rectángulo: "))
            altura = float(input("Ingresa la altura del rectángulo: "))
            figura = figuritas(fig=3, b=base, h=altura)
            calculo = input("¿Qué quieres calcular? (a para área, p para perímetro): ").lower()
            resultado = figura.rectangulo(opc=calculo)
            print(f"El resultado es: {resultado:.2f}\n")

        elif opcion == "4":
            # --- Pedir datos para el Polígono Regular ---
            lados = int(input("Ingresa el número de lados: "))
            medida_lado = float(input(f"Ingresa la medida de uno de los {lados} lados: "))
            apotema = float(input("Ingresa la medida del apotema: "))
            figura = figuritas(fig=4, medida=medida_lado, nolados=lados, ap=apotema)
            calculo = input("¿Qué quieres calcular? (a para área, p para perímetro): ").lower()
            resultado = figura.poligono(opc=calculo)
            print(f"El resultado es: {resultado:.2f}\n")

        elif opcion == "5":
            print("¡Adiós!")

        else:
            print("Opción no válida. Inténtalo de nuevo.\n")

    except ValueError:
        print("Error: Ingresaste un valor no numérico. Intenta de nuevo.\n")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}\n")