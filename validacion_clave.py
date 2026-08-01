clave = "python123"
intentos = 0

while intentos < 3:

    dato = input("Ingrese la clave: ")

    if dato == clave:
        print("Acceso permitido")
        break
    else:
        intentos += 1
        print("Acceso denegado")

if intentos == 3:
    print("Ha excedido el numero de intentos")