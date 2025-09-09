import generarReportes
def descargar_material_academico(estudiante_id, curso_id, nombre_archivo):
    """
    Simula la descarga de material académico para un estudiante.

    :param estudiante_id: ID del estudiante.
    :param curso_id: ID del curso.
    :param nombre_archivo: Nombre del archivo a descargar.
    :return: Mensaje de confirmación.
    """
    # Lógica para buscar y "descargar" el archivo
    print(f"El estudiante {estudiante_id} ha descargado el material '{nombre_archivo}' del curso {curso_id}.")
    return f"Descarga exitosa: {nombre_archivo}"

# Ejemplo de uso
descargar_material_academico("E001", "C001", "Introduccion_a_Python.pdf")
