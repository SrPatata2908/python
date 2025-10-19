#Perimetro
radio = float(input("Dame Tu Radio: "))
from math import pi 
peri = 2*pi*radio
area = pi*(radio**2)
periredo =round(peri, 2)
arearedo =round(area, 2)
print ("Su perimetro es:", periredo, "y area es:", arearedo)