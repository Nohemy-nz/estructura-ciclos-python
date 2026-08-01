
n = int(input("Ingrese un numero: "))

invertido = 0

while n > 0:
    invertido = invertido * 10 + n % 10
    n = n // 10

print(invertido)
