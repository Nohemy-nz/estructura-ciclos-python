num = int(input("ingrese el numero para el factorial: "))

if num < 0:
    print("No se puede calcular el factorial")
else:
    factorial = 1
    inferiores = 1
while True:
        factorial = factorial * inferiores
        inferiores = inferiores + 1

        if inferiores > num:
            break

print("Factorial de", num, "es", factorial)
   