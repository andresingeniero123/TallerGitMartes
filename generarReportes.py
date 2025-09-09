import descargarmaterialacademico as pd

def generar_reporte_excel(curso, profesor, semestre, datos_estudiantes):
    """
    Genera un reporte académico en formato Excel.

    :param curso: Nombre del curso.
    :param profesor: Nombre del profesor.
    :param semestre: Semestre actual.
    :param datos_estudiantes: Lista de diccionarios con datos de los estudiantes.
    :return: Archivo Excel generado.
    """
    df = pd.DataFrame(datos_estudiantes)
    nombre_archivo = f"Reporte_{curso}_{profesor}_{semestre}.xlsx"
    df.to_excel(nombre_archivo, index=False)
    print(f"Reporte generado: {nombre_archivo}")
    return nombre_archivo

# Ejemplo de uso
datos_ejemplo = [
    {"Estudiante": "Andrés Moncayo", "Nota": 4.5},
    {"Estudiante": "Ana Gómez", "Nota": 5.0}
]
generar_reporte_excel("Ingeniería de Software", "Profesor Pérez", "2025-2", datos_ejemplo)
