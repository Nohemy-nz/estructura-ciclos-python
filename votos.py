votos_Android = 0
votos_Ios = 0
while True:
    codigoEstudiante = input("Ingrese codigo del estudiante: ")
    voto = input("Ingrese su eleccion Android - Ios: ")

    if voto == "Android":
        votos_Android += 1
    elif voto == "Ios":
        votos_Ios += 1
    else:
        print("Opcion no valida")

    if voto != "Android" and voto != "Ios":
        break
    print("Votos para Android:", votos_Android)
    print("Votos para Ios:", votos_Ios)

    if votos_Android > votos_Ios:
        print("Android gano")
    elif votos_Ios > votos_Android:
        print("Ios gano")
    else:
        print("Empate")