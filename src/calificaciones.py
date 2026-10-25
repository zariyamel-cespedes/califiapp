LIMITE_ALUMNOS = 30
MINIMA_APROBATORIA = 6

# calificaciones.py - Lógica de CalifiApp (una función por criterio)
# Cada función responde a un criterio de aceptación de las HU-01 a HU-04.


# HU-01 Registrar alumnos
def registrar_alumno(alumnos, nombre):
    nombre = nombre.strip()
    if nombre == "" or len(alumnos) >= LIMITE_ALUMNOS:
        return False
    alumnos.append(nombre)
    return True


# HU-02 Capturar calificaciones
def validar_calificacion(texto):
    try:
        calificacion = float(texto)
    except ValueError:
        return None
    if calificacion < 0 or calificacion > 10:
        return None
    return calificacion


# HU-03 Calcular promedio y estatus
def calcular_promedio(calificaciones):
    return round(sum(calificaciones) / len(calificaciones), 1)


def obtener_estatus(promedio):
    if promedio >= MINIMA_APROBATORIA:
        return "APROBADO"
    return "REPROBADO"


# HU-04 Mostrar reporte del grupo
def fila_reporte(nombre, promedio):
    return nombre + " | " + str(promedio) + " | " + obtener_estatus(promedio)


def promedio_grupal(promedios):
    if len(promedios) == 0:
        return 0.0
    return round(sum(promedios) / len(promedios), 1)
