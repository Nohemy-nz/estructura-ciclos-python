
cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))

contador_estudiantes = 0
aprobados = 0
reprobados = 0
suma_definitiva = 0
while contador_estudiantes < cantidad_estudiantes:
    codigo_estudiante = input("Ingrese el código del estudiante: ")
    nota_definitiva = float(input("Ingrese la nota definitiva: "))

    if nota_definitiva >= 3.0:
        aprobados += 1  
    else:
        reprobados += 1
    suma_definitiva += nota_definitiva
    contador_estudiantes += 1
promedio_grupo = suma_definitiva / cantidad_estudiantes

print("Cantidad de estudiantes aprobados:", aprobados)
print("Cantidad de estudiantes reprobados:", reprobados)
print("Promedio del grupo:", promedio_grupo)