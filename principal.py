from AgregarGrado import Grado

grados = {}

def agregar_grado():
    codigo = input("Ingrese código de grado: ")
    if codigo in grados:
        print("El código ya existe.")
        return
    nombre = input("Ingrese nombre del grado: ")
    grados[codigo] = Grado(codigo, nombre)
    print("...Se agregó el grado exitosamente\n")

def inscribir_alumno():
    if not grados:
        print("No hay grados disponibles. Agregue uno primero.\n")
        return

    apellidos = input("Ingrese Apellidos: ")
    nombre = input("Ingrese Nombre: ")

    print("...Seleccione el grado en el que inscribirá al alumno")
    for codigo, grado in grados.items():
        print(f"{codigo} {grado.nombre}")
    codigo = input("Ingrese el código del grado: ")

    grado = grados.get(codigo)
    if not grado:
        print("Código de grado no válido.\n")
        return

    if grado.agregar_alumno(nombre, apellidos):
        print("...Alumno inscrito exitosamente\n")
    else:
        print("Este grado ya tiene el máximo de 3 alumnos.\n")

def ver_alumnos_por_grado():
    if not grados:
        print("No hay grados registrados.\n")
        return

    for codigo, grado in grados.items():
        print(f"\nGrado: {grado.nombre} ({codigo})")
        print(grado.mostrar_alumnos())

def menu():
    while True:
        print("1. Agregar Grado")
        print("2. Inscribir Alumno")
        print("3. Ver Alumnos por Grado")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_grado()
        elif opcion == "2":
            inscribir_alumno()
        elif opcion == "3":
            ver_alumnos_por_grado()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.\n")

if __name__ == "__main__":
    menu()
