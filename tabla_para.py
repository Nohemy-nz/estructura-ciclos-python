while True:
    cantidad_numero = int(input("ingrese la cantidad de numeros: "))
    if cantidad_numero > 0:
        for num in range(1, cantidad_numero + 1):
            print(num, "  ", num * num, "   ", num + num * num)