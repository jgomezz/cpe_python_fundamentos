'''
print('----------- Primera Version ------------------')

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

'''

print('----------- Segunda Version ------------------')


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
    
    def __init__(self, nombre, apellido, ciudad, especialidad):
        super().__init__(nombre, apellido, ciudad) # Llamada al constructor de la clase base    
        self.especialidad = especialidad

    def obtener_residencia(self):
        return f"El administrador {self.nombre} vive en {self.ciudad} "

    def obtener_nombre_completo(self):
        return "Es una informacion confidencial"


class Desarrollador(Empleado):
    
    def __init__(self, nombre, apellido, ciudad, experto_lenguaje_prog):
        super().__init__(nombre, apellido, ciudad) # Llamada al constructor de la clase base    
        self.experto_lenguaje_prog = experto_lenguaje_prog

    def obtener_experiencia(self):
        return f"El desarrollador {self.nombre} es experto en {self.experto_lenguaje_prog}"



class Instructor(Empleado):
    
    def __init__(self, nombre, apellido, ciudad, anhos_exp, nombre_curso):
        super().__init__(nombre, apellido, ciudad) # Llamada al constructor de la clase base    
        self.anhos_exp = anhos_exp
        self.nombre_curso = nombre_curso

    def obtener_exp_instructor(self):
        return f"El instructor {self.nombre} tiene {self.anhos_exp} años de experiencia y dicta el curso de {self.nombre_curso}"

print('----------- Administrador ------------------')

admin = Administrador("Juan","Sanchez","Lima","Redes")
print(admin.obtener_residencia())
print(admin.obtener_nombre_completo())

print('----------- Desarrollador ------------------')

des = Desarrollador("Jaime","Gomez","Trujillo","Python")
print(des.obtener_experiencia())

print('----------- Instructor ------------------')

instructor = Instructor("Maria","Perez","Arequipa",5,"IA")
print(instructor.obtener_exp_instructor())