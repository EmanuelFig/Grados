class Alumno:
    def __init__(self, nombre,apellidos):
        self.nombre = nombre 
        self.Apellidos = apellidos

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, value):
        self.nombre = value

    def get_Apellidos(self):
        return self.Apellidos

    def set_Apellidos(self, value):
        self.Apellidos = value

        
    def __str__(self):
        return f"{self.Apellidos},{self.nombre}"
    
