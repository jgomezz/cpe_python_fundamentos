
# Clase Base
class Empleado:

    def __init__(self, nombre, apellido, ciudad):
        self.nombre = nombre
        self.apellido = apellido
        self.ciudad = ciudad

    def obtener_nombre_completo(self):
        return self.nombre + " " + self.apellido
    

# Clase hijas

class Administrador(Empleado):
    pass

class Desarrollador(Empleado):
    pass

class Instructor(Empleado):
    pass


admin = Administrador("Juan","Sanchez","Lima")

des = Desarrollador("Jaime","Gomez","Trujillo")

instructor = Instructor("Maria","Perez","Arequipa")


print(admin.obtener_nombre_completo())
print(des.obtener_nombre_completo())
print(instructor.obtener_nombre_completo())