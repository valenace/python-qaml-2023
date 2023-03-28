def agregar_curso(listado: list):
    print("AGREGAR CURSO")
    nombre_curso = input("Nombre del curso: ")
    alumnos_curso = input("Cantidad de alumnos: ")
    clases_curso = input("Cantidad de clases: ")
    status_curso = input(f"Estado del curso {' , '.join(ESTADOS_VALIDOS) }: ")
    if status_curso in ESTADOS_VALIDOS:
        course = {
            "nombre_curso": nombre_curso,
            "total_alumnos": alumnos_curso,
            "total_clases": clases_curso,
            "status_curso": status_curso
        }
        listado.append(course)
        print("Curso agregado")
        ver_curso(course)
    else:
        print(f"Estado no valido: {status_curso}")


def buscar_curso(listado: list):
    print("BUSCAR CURSO")
    termino = input("Nombre del curso: ")
    busqueda = [course for course in listado if course["nombre_curso"] == termino]
    if busqueda and len(busqueda) > 0:
        print(f"Curso encontrado!")
        ver_curso(busqueda[0])
        update = input(f"Actualizar? (SI | NO)")
        if update == "SI":
            update_cursos(busqueda[0])
    else:
        print("Curso no encontrado")


def mostrar_cursos(listado: list):
    nombre_cursos = [course["nombre_curso"] for course in listado]
    print(f"CURSOS: {nombre_cursos}")
    show_details = input("Mostrar detalles? (SI | NO)")
    if show_details == "SI":
        for course in listado:
            ver_curso(course)


def update_cursos(course: dict):
    print("ACTUALIZAR CURSO")
    status_curso = input(f"Estado? {' | '.join(ESTADOS_VALIDOS) }")
    if status_curso in ESTADOS_VALIDOS:
        course["status_curso"] = status_curso
        print("Curso actualizado")
        ver_curso(course)
    else:
        print(f"Estado no valido: {status_curso}")


def ver_curso(course: dict):
    print(f"Curso: {course['nombre_curso']}, Estado: {course['status_curso']}")


def salir(listado: list):
    print("CLOSING...")
    print(f"Cursos: {listado}")
    exit(0)


ESTADOS_VALIDOS = ("No Iniciado", "Activo")
CURSOS = []
MENU = {
    "AGREGAR": agregar_curso,
    "ACTUALIZAR": buscar_curso,
    "MOSTRAR": mostrar_cursos,
    "SALIR": salir
}

while True:
    for option, method in MENU.items():
        action = input(f"¿Qué deseas realizar: {' | '.join(MENU.keys())}?\n")
        if action in MENU.keys():
            MENU[action](CURSOS)
        else:
            print(f"Acción inválida: {action}")