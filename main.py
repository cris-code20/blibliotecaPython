
biblioteca = []
prestamos = {}

# voy atrabajar bajo el paradigma de programacion funcional la cual consta de crear funciones al 
# inicio del projecto y utilizarlas mas abajo. Usaremos las listas para crear el flujo de datos.

# Vamos a crear la funcion que se encarge de gestionar los libros prestados
def registrar_prestamo():
    codigo = input("Ingrese el código del libro a prestar: ")
    for libro in biblioteca:
        if libro["codigo"] == codigo:
            if prestamos.get(codigo) == "prestado":
                print("El libro ya está prestado.")
            else:
                prestamos[codigo] = "prestado"
                print(f"Libro '{libro['titulo']}' prestado con éxito.")
            return
    print("Libro no encontrado en la biblioteca.")


def renovar_prestamo():
    codigo = input("Ingrese el código del libro a renovar: ")
    if prestamos.get(codigo) == "prestado":
        print("Préstamo renovado con éxito.")
    else:
        print("El libro no está prestado.")


def devolver_libro():
    codigo = input("Ingrese el código del libro a devolver: ")
    if prestamos.get(codigo) == "prestado":
        prestamos[codigo] = "en sala"
        print("Libro devuelto con éxito.")
    else:
        print("El libro no está prestado o no existe en los registros.")


def verificar_salida_irregular():
    codigo = input("Ingrese el código del libro: ")
    estado = prestamos.get(codigo, "en sala")
    if estado == "en sala":
        print(f"¡Alerta! El libro '{codigo}' está saliendo con estado 'en sala'.")
    else:
        print(f"El libro '{codigo}' tiene estado '{estado}' y está permitido salir.")

# en esta parte vamos a manejar el crud y el menu
def menu():
    while True:
        print("\nSistema de Biblioteca (Extendido)")
        print("1. Guardar libro")
        print("2. Modificar libro")
        print("3. Consultar libros")
        print("4. Buscar libro por código")
        print("5. Eliminar libro")
        print("6. Registrar préstamo")
        print("7. Renovar préstamo")
        print("8. Devolver libro")
        print("9. Verificar salida irregular")
        print("10. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            guardar_libro()
        elif opcion == "2":
            modificar_libro()
        elif opcion == "3":
            consultar_libros()
        elif opcion == "4":
            buscar_libro()
        elif opcion == "5":
            eliminar_libro()
        elif opcion == "6":
            registrar_prestamo()
        elif opcion == "7":
            renovar_prestamo()
        elif opcion == "8":
            devolver_libro()
        elif opcion == "9":
            verificar_salida_irregular()
        elif opcion == "10":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


def guardar_libro():
    codigo = input("Ingrese el código del libro: ")
    titulo = input("Ingrese el título del libro: ")
    apellido_autor = input("Ingrese el apellido del autor: ")
    nombre_autor = input("Ingrese el nombre del autor: ")
    area_conocimiento = input("Ingrese el área de conocimiento: ")
    publicador = input("Ingrese el publicador: ")
    tramo_asignado = input("Ingrese el tramo asignado: ")
    
    libro = {
        "codigo": codigo,
        "titulo": titulo,
        "apellido_autor": apellido_autor,
        "nombre_autor": nombre_autor,
        "area_conocimiento": area_conocimiento,
        "publicador": publicador,
        "tramo_asignado": tramo_asignado
    }
    biblioteca.append(libro)
    print("Libro guardado con éxito.")

def modificar_libro():
    codigo = input("Ingrese el código del libro a modificar: ")
    for libro in biblioteca:
        if libro["codigo"] == codigo:
            print("Libro encontrado. Ingrese los nuevos datos:")
            libro["titulo"] = input("Nuevo título: ")
            libro["apellido_autor"] = input("Nuevo apellido del autor: ")
            libro["nombre_autor"] = input("Nuevo nombre del autor: ")
            libro["area_conocimiento"] = input("Nueva área de conocimiento: ")
            libro["publicador"] = input("Nuevo publicador: ")
            libro["tramo_asignado"] = input("Nuevo tramo asignado: ")
            print("Libro modificado con éxito.")
            return
    print("Libro no encontrado.")

def consultar_libros():
    if not biblioteca:
        print("No hay libros registrados.")
    else:
        for libro in biblioteca:
            print(f"Código: {libro['codigo']}, Título: {libro['titulo']}")

def buscar_libro():
    codigo = input("Ingrese el código del libro a buscar: ")
    for libro in biblioteca:
        if libro["codigo"] == codigo:
            print(f"Libro encontrado: Código: {libro['codigo']}, Título: {libro['titulo']}")
            return
    print("Libro no encontrado.")

def eliminar_libro():
    codigo = input("Ingrese el código del libro a eliminar: ")
    for libro in biblioteca:
        if libro["codigo"] == codigo:
            biblioteca.remove(libro)
            print("Libro eliminado con éxito.")
            return
    print("Libro no encontrado.")


# Ejecución del programa
if __name__ == "__main__":
    menu()