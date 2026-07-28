num = int (input("ingrese numero: "))
if num > 0:
    copia_num = num
    contador_c = 0
    suma = 0

    while num >0:
        cifra = copia_num % 10
        copia_num = copia_num // 10
        suma += cifra
        contador_c += 1

    print("La cantidad de cifras es:", contador_c)
    print("La suma de las cifras es:", suma)
else:
    print("El numero no es positivo")


