print ("Detector de pares y impares")
pire = int(input("Ingresa de donde quieres empezar: "))
impire = int(input("Ingresa de donde quires acabar: "))
par = 0
impar = 0
for numero in range (pire, impire):
    if numero %2 == 0:
        par += 1 
    else:
        impar += 1
print(f"Se tiene {par} numeros pares")
print(f"Se tiene {impar} numeros impares")