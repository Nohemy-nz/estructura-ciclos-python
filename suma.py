suma = 0

while True:
    n = int(input("Ingrese un numero: "))

    if n == 0:
        break

    if n < 0:
        continue

    suma += n

print("La suma es:", suma)