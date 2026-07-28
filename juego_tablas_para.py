seguir = "S"

while seguir == "S" or seguir == "s":

    print("¿Con cuál tabla desea jugar?")

    while True:
        tabla = int(input())
        if tabla > 1 and tabla < 20:
            break
        print("Ingrese una tabla entre 2 y 19:")

    aciertos = 0
    desaciertos = 0

    for contadorFilas in range(1, 11):
        producto = tabla * contadorFilas

        respuesta = int(input(f"Escriba el resultado de: {tabla} x {contadorFilas}: "))

        if respuesta == producto:
            print("¡Felicidades!")
            aciertos += 1
        else:
            print("Lo siento, ese no es el resultado.")
            print("La respuesta correcta es:", producto)
            desaciertos += 1

    print("\nAciertos:", aciertos)
    print("Desaciertos:", desaciertos)

  
    if aciertos <= 5:
        print("Insuficiente")
    elif aciertos <= 7:
        print("Aceptable")
    elif aciertos <= 9:
        print("Sobresaliente")
    else:
        print("Excelente")

   
    while True:
        seguir = input("¿Desea volver a jugar? [S/N]: ")
        if seguir in ("S", "s", "N", "n"):
            break
        