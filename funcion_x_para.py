while True:
    valor_x = int(input("Ingrese el máximo valor para x: "))
    if valor_x > 0:
        break
    print("El valor debe ser mayor que 0.")

for x in range(0, valor_x + 1, 2):
    fun = x**3 + x**2 - 5
    print("Para x =", x, "f(x) =", fun)