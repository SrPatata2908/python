class cuenta_bancaria:
    def __init__ (self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def deposito (self, monto):
        self.saldo += monto
    def retirar (self, monto):
        self.saldo -= monto
        print(f"Retiro de ${monto:.2f} realizado con éxito.")
    def mostrar_saldo(self):
        return self.saldo
    def mostrar_titular(self):
        return self.titular
    
print("Inicializemos tu cuenta bancaria")    
nombre = input("Ingresa el nombre del titular: ")
iniciar = int(input("Dame el saldo inicial: "))
mi_cuenta = cuenta_bancaria (nombre, iniciar)
opc = 0
while True:
    
    print("1 PARA DEPOSITAR")
    print("2 PARA RETIRAR")
    print("3 PARA SALIR")
    opc=int(input("Eligue una de las acciones"))
    match opc:
        case 1:
        
            print("Hola ",mi_cuenta.mostrar_titular(), "tu saldo inicial es ",mi_cuenta.mostrar_saldo())
            monto = int(input(f"Cuanto deseas ingresar: "))
            mi_cuenta.deposito(monto)
            print(f"Depósito de ${monto:.2f} realizado con éxito.")
            print(f"tu saldo actual es {mi_cuenta.mostrar_saldo()}")
        case 2: 
             print("Hola ",mi_cuenta.mostrar_titular(), "tu saldo inicial es ",mi_cuenta.mostrar_saldo())
             monto = int(input(f"Cuanto deseas retirar: "))
             mi_cuenta.retirar(monto)
             print(f"Retiro de ${monto:.2f} realizado con éxito.")
             print(f"tu saldo actual es {mi_cuenta.mostrar_saldo()}")
        case 3: break
        case __: print("opcion no reconocida")        
