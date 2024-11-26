from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"  # Set default value for class attribute

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes=None, **kwargs):
        self._grupo = grupo
        self._asignaturas = asignaturas if asignaturas is not None else []
        self.listadoAlumnos = estudiantes if estudiantes is not None else []

    @classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre