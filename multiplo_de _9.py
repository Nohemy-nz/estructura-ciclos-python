n = int(input("Ingrese inicio del rango: "))
m = int(input("Ingrese fin del rango: "))

encontrado = False

for i in range(n, m + 1):

    if i % 9 == 0:
        print(i, "es el primer multiplo de 9")
        encontrado = True
        break

if encontrado == False:
    print("No hay multiplos de 9")