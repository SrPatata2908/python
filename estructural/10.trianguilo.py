#triangulo
print("Adivinador de triangulo")
ladoa = int(input("Escribe tu lado A: "))
ladob = int(input("Escribe tu lado B: "))
ladoc = int(input("Escribe tu lado C: "))
if(ladoa == ladob and ladob == ladoc):
    print("Es equilatero")
elif((ladoa == ladob and ladoc != ladoc) or (ladoa == ladoc and ladob != ladoa) or (ladob == ladoc and ladoa !=ladoc)):
    print("Es Isosele")
elif (ladoa != ladob and ladob != ladoc):
    print("Es Escaleno")