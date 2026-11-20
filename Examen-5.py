num_estudiantes = int(input("Cantidad de estudiantes: "))
num_materias = int(input("Cantidad de materias: "))


while num_estudiantes <= 0 or num_materias <= 0:
    print("Error: las cantidades deben ser mayores a cero.")
    num_estudiantes = int(input("Cantidad de estudiantes: "))
    num_materias = int(input("Cantidad de materias: "))


matriz = []

for i in range(num_estudiantes):

    fila = []

    print(f"\nEstudiante {i + 1}")

    for j in range(num_materias):

        calificacion = float(input(f"Calificación de materia {j + 1}: "))

        while calificacion < 0 or calificacion > 100:
            print("Error: la calificación debe estar entre 0 y 100.")
            calificacion = float(input(f"Calificación de materia {j + 1}: "))

        fila.append(calificacion)

    matriz.append(fila)



for i in range(num_estudiantes):

    suma = 0

    for j in range(num_materias):
        suma += matriz[i][j]

    promedio = suma / num_materias

    print(f"Estudiante {i + 1}: {promedio:.2f}")


for j in range(num_materias):

    suma = 0

    for i in range(num_estudiantes):
        suma += matriz[i][j]

    promedio = suma / num_estudiantes

    print(f"Materia {j + 1}: {promedio:.2f}")


mayor = matriz[0][0]
menor = matriz[0][0]

for i in range(num_estudiantes):

    for j in range(num_materias):

        if matriz[i][j] > mayor:
            mayor = matriz[i][j]

        if matriz[i][j] < menor:
            menor = matriz[i][j]



print("Calificación más alta:", mayor)
print("Calificación más baja:", menor)


for i in range(num_estudiantes):

    print(f"Estudiante {i + 1}:", matriz[i])



