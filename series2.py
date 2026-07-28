cantidadTerminos = int(input("Ingrese la cantidad de términos a generar: "))

contadorNumeros = 0
termino = 1

while True:
    print(termino, end=", ")

    termino = termino + 2
    contadorNumeros = contadorNumeros + 1

    if contadorNumeros > cantidadTerminos - 1:
        break

print(termino)