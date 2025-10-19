#IMC
peso = float(input("Dame tu peso: "))
esta = float(input("Dame tu estatura: "))
imc = peso/esta**2
imc_redo =round(imc, 2)
if (imc <= 18.49):
    print("Peso Bajo, tu imc es de", imc_redo)
if (imc >= 18.50 and imc <=24.99):
    print("Peso normal, Tu imc es de:", imc_redo)
if (imc >= 25 and imc <=29.99):
    print("Es Sobrepeso, Tu imc es de:", imc_redo)
if (imc >= 30 and imc <=34.99):
    print("Es Obesidad leve, Tu imc es de:", imc_redo)
if (imc >= 35 and imc <=39.99):
    print("Es Obesidad Media, Tu imc es de:", imc_redo)
if (imc >= 40):
    print("Es Obesidad Morbida, Tu imc es de:", imc_redo)
