cantidad_terminos = int(input("Ingrese la cantidad de terminos a generar: "))
contador_numeros = 0
termino = 1

while contador_numeros < cantidad_terminos - 1:
    print(termino, end=", ")
    termino = termino + 2
    contador_numeros = contador_numeros + 1
print(termino)



'''Mientras ( contadorNumeros < cantidadTerminos - 1)
		Escribir termino , ", "
		termino = termino + 2
		contadorNumeros = contadorNumeros + 1
	FinMientras
	Escribir  termino
FinAlgoritmo'''