import random


class aho:
    def __init__ (self, palabrota):
        self.palabrota = palabrota.upper()
        self.vector = list("_" * len(self.palabrota))
        self.intentos = 7
        
    
    def imprime (self):
        for letrita in self.vector:
            print(letrita, end=" ")
        print()

    def adivinar(self):
        print("Adivina")
        
        while "_" in self.vector and self.intentos >0:
            self.imprime()
            print(f"Quedan {self.intentos} intentos")
            let = input("Pon una letra: ").upper()

            if let in self.palabrota:
                print("Si esta la letra")
                for letrita in range(len(self.palabrota)):
                    if self.palabrota[letrita] == let:
                        self.vector[letrita] = let
            else:
                print("No esta la letra")
                self.intentos -= 1
        print(f"La palabra era {obj.palabrota}")

with open('oficina.txt', 'r', encoding='utf-8') as archivo:
     palabras = archivo.read().splitlines()
     random = random.choice(palabras)

mis = random
obj = aho(mis.upper())
obj.adivinar()
