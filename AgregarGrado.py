from AgregarAlumno import Alumno

class Grado:
    LIMITE_ALUMNOS = 3

    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.alumnos = []

    def agregar_alumno(self, nombre, apellidos):
        if len(self.alumnos) < Grado.LIMITE_ALUMNOS:
            nuevo_alumno = Alumno(nombre, apellidos)
            self.alumnos.append(nuevo_alumno)
            return True
        else:
            return False

    def mostrar_alumnos(self):
        if not self.alumnos:
            return "No hay alumnos inscritos."
        return "\n".join([str(alumno) for alumno in self.alumnos])

    def __str__(self):
        return f"{self.codigo} {self.nombre}"
              
    
