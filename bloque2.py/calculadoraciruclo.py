import math
class figuritas:
    def __init__(self, fig, r=None, l1=None, l2=None, l3=None, b=None, h=None, medida= None, nolados= None, ap=None):
        match (fig):
            case 1: #circulo
                self.r = r
            case 2: #triangulo
                self.l1 = l1
                self.l2 = l2
                self.l3 = l3
                self.b = b
                self.h = h
            case 3: #rectangulo 
                self.b=b
                self.h=h
            case 4: # poligono
                self.medida = medida
                self.nolados = nolados
                self.ap = ap
    def circulo(self, opc):
        self.opc = opc
        res=0
        if (opc=="a"):
            res = math.pi * self.r**2
        if (opc=="p"):
            res= 2*math.pi*self.r
        return res
    def triangulo (self, opc):
        self.opc = opc
        res = 0
        if (opc=="p"):
            res = self.l1+self.l2+self.l3
        if (opc=="a"):
            res = self.b*self.h/2
        return res
    def rectangulo(self, opc):
        self.opc = opc
        res=0
        if (opc=="a"):
            res= self.b*self.h
        if (opc=="p"):
              res = 2*self.b+2*self.h
        return res
    def poligono (self, opc):
        self.opc = opc
        res = 0
        peri = self.medida * self.nolados
        are = (self.peri*self.ap)
        if (opc == "a"):
            res = are
        if (opc== "p"):
            res = peri
        return res

def menu():
    print("Calculadora casera y chida ")
    print("1. Círculo, 2. Triangulo, 3. Rectangulo, 4. Poligono")
    fig = int(input("Elige la figura a calcular: "))
    
    opc = input("Que nesecitas: (a: area o p: perímetro): ").lower()

    if fig == 1:
        r = float(input("Radio del círculo: "))
        forma = figuritas(fig=1, r=r)
        print("Resultado:", forma.circulo(opc))

    elif fig == 2:
        b = float(input("Base: "))
        h = float(input("Altura: "))
        l1 = float(input("Lado 1: "))
        l2 = float(input("Lado 2: "))
        l3 = float(input("Lado 3: "))
        forma = figuritas(fig=2, b=b, h=h, l1=l1, l2=l2, l3=l3)
        print("Resultado:", forma.triangulo(opc))

    elif fig == 3:
        b = float(input("Base: "))
        h = float(input("Altura: "))
        forma = figuritas(fig=3, b=b, h=h)
        print("Resultado:", forma.rectangulo(opc))

    elif fig == 4:
        medida = float(input("Medida del lado: "))
        nolados = int(input("Número de lados: "))
        ap = float(input("Apotema: "))
        forma = figuritas(fig=4, medida=medida, nolados=nolados, ap=ap)
        print("Resultado:", forma.poligono(opc))

    else:
        print("Elige una opcion correcta")
menu()
