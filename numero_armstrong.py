# Pedir un número
num = int(input("Ingrese un número: "))

replica = num
cifra = 0

while replica > 0:
    cifra = cifra + 1
    replica = replica // 10

replica = num
suma = 0

while replica > 0:
    digito = replica % 10
    suma = suma + digito ** cifra
    replica = replica // 10

if suma == num:
    print("Sí es un número de Armstrong.")
else:
    print("No es un número de Armstrong.")