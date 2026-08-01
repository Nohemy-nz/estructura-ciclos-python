cantidadTerminos = int(input("Ingrese la cantidad de terminos a generar: "))
termino = 1
for contadorNumeros in range(1, cantidadTerminos):
    print(termino, end=", ")
    termino = termino + 2
print(termino)

