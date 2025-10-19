class indice: 
    def __init__ (self, altura, peso):
        self.peso = peso
        self.altura = altura
    def calcular_imc (self):
        imc = self.peso / self.altura**2
        return imc
    def mostrar_resultados (self, imc):
        self.imc = imc 
        res = ""
        if (imc <= 18.49):
         res ="Peso Bajo"
        elif (imc >= 18.50 and imc <=24.99):
         res=("Peso normal")
        elif (imc >= 25 and imc <=29.99):
         res=("Es Sobrepeso")
        elif (imc >= 30 and imc <=34.99):
           res=("Es Obesidad leve")
        elif (imc >= 35 and imc <=39.99):
         res=("Es Obesidad Media", )
        elif (imc >= 40):
         res= ("Es Obesidad Morbida", )
        return res

peso = float(input("Ingresa tu peso: "))
altura = float(input("Ingresa tu altura: "))
salud = indice(altura, peso)
imc=salud.calcular_imc()
print(f"Tu imc es de {salud.mostrar_resultados(imc)}")
