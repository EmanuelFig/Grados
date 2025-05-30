from AgregarAlumno import Alumno

class Grado:

    LIMITE_ALUMNOS = 3

    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.alumnos = []

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, value):
        self.nombre = value

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, value):
        self.codigo = value

    def get_alumnos(self):
        return self.alumnos

    def set_alumnos(self, value):
        self.alumnos = value


    def agregar_alumno(self,nombre, apellidos):
        if len(self.alumnos) < Grado.LIMITE_ALUMNOS:
            nuevoAlumno = Alumno(nombre,apellidos)
            self.alumnos.append(nuevoAlumno)

            return True

        else:

            return False

    def mostrar_alumnos(self):
        if not self.alumnos:
            return "No Hay alumnos Inscritos"

    def __str__(self):
        return f"{self.codigo},{self.nombre}"
              
    