n = int(input("Ingrese un numero: "))

while n >= 0:

    print(n)

    if n != 0 and n % 7 == 0:
        print(n, "es un multiplo de 7")

    n -= 1