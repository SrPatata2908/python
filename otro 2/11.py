#hacer un programa que pida un numero positivo al usuario y realice la suma de los numeros pares unicamente del cero al numero dado
class numerito:
    def __init__ (self, numero):
        self.numero = numero

    def par (self):
        suma = 0
        for xd in range(0, self.numero + 1):
            if xd % 2 == 0:
                suma += xd
        return suma

dd_str = input("Di tu numero positivo: ")
dd = int(dd_str) 
mi_numero = numerito(dd)
print(f" La suma de los números pares hasta es: {mi_numero.par()}")