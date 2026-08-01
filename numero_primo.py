n = int(input("Ingrese un numero: "))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("El numero no es primo")
            break
    else:
        print("El numero es primo")
else:
    print("El numero debe ser mayor que 1")