while True:

    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")

    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        a = int(input("Primer numero: "))
        b = int(input("Segundo numero: "))
        print("Resultado:", a + b)

    elif opcion == 2:
        a = int(input("Primer numero: "))
        b = int(input("Segundo numero: "))
        print("Resultado:", a - b)

    elif opcion == 3:
        print("Programa finalizado")
        break

    else:
        print("Opcion no valida")