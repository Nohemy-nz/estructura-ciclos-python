cantidadTerminos = int(input("Ingrese la cantidad de terminos a generar: "))
termino = 1
for contadorNumeros in range(1, cantidadTerminos):
    print(termino, end=", ")
    termino = termino + 2
print(termino)







'''Algoritmo seriePara
	definir catidadTerminos, contadorNumeros, termino Como Entero
	imprimir "Ingrese la catntidad de terminos a generar: "
	leer cantidadTerminos
	termino = 1
	Para contadorNumeros = 1 Hasta cantidadTerminos - 1 con paso 1 Hacer
		imprimir termino, "  ,  "
		termino = termino + 2
	FinPara
	imprimir termino
FinAlgoritmo'''