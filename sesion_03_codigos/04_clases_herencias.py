'''
Curso : Programacion Basica de Python
Sesion : 03
Tema : Introduccion a Python -  Herencia
Author : Jaime Gomez

'''

'''
Para debug en mac : export LC_ALL=C
'''

#''' Primera version  : Herencia Simple

# Clase Base
class Empleado:

    def __init__(self, nombre, apellido):
        super().__init__()
        self.nombre = nombre
        self.apellido = apellido
        
    def nombre_completo(self):
        return self.nombre + " " + self.apellido


# Clase hija
class Desarrollador(Empleado):
    pass

emp_01 = Empleado("Juan","Acosta")
print(emp_01.nombre_completo())

des_01 = Desarrollador("Jaime","Gomez")
print(des_01.nombre_completo())


'''
Ejercicio 1:
Agregar el atributo ciudad en la clase base
(constructor) y usarlo en la clase hija

Ejercicio 2:
Crear la clase hija Administrador que tiene
como clase base a Empleado e instanciar un 
objeto

'''

# Clase Base
class Empleado:

    def __init__(self, nombre, apellido, 
                ciudad = "Trujillo"):
        super().__init__()
        self.nombre = nombre
        self.apellido = apellido
        self.ciudad = ciudad
        
    def nombre_completo(self):
        return self.nombre + " " + self.apellido + " " + self.ciudad

 # Clase hija
class Desarrollador(Empleado):
    pass

class Admin(Empleado):
    pass

emp_01 = Empleado("Juan","Acosta","Lima")
print(emp_01.nombre_completo())
des_01 = Desarrollador("Jaime","Gomez")
print(des_01.nombre_completo(),' es de: ',des_01.ciudad)

admin_01 = Admin('Juan','Sanchez')
print(admin_01.nombre_completo())


#'''

#''' Segunda version  : Herencia Simple

# Clase Base
class Empleado:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def nombre_completo(self):
        return self.nombre + " " + self.apellido

# Clase hija
class Desarrollador(Empleado):

    def nombre_completo(self):
        return self.nombre.upper() \
            + " " + self.apellido.upper()

emp_01 = Empleado("Juan","Acosta")
print(emp_01.nombre_completo())

des_01 = Desarrollador("Jaime","Gomez")
print(des_01.nombre_completo())

'''
Crear en la clase base Empleado
el metodo obtener_usuario que me retorne
el primer caracter del nombre concatenado
con el apellido, todo en minuscula

En la clase hija Desarrollador el 
metodo obtener_usuario debe devolver 
el primer caracter del apellido 
concatenado con el nombre, todo en mayuscula

'''


# Clase Base
class Empleado:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def nombre_completo(self):
        return self.nombre + " " + self.apellido

    def obtener_usuario (self):
        return self.nombre[0].lower() + self.apellido.lower()

# Clase hija
class Desarrollador(Empleado):

    def nombre_completo(self):
        return self.nombre.upper() + " " + self.apellido.upper()
    
    def obtener_usuario (self):
        return self.apellido[0].upper()  + self.nombre.upper()

#emp_01 = Empleado("Juan","Acosta")
#print(emp_01.nombre_completo())
#des_01 = Desarrollador("Jaime","Gomez")
#print(des_01.nombre_completo())
emp_01 = Empleado("Juan","Acosta") # jacosta
print(emp_01.obtener_usuario())
des_01 = Desarrollador("Jaime","Gomez") #GJAIME
print(des_01.obtener_usuario())


'''



#'''

#''' Tercera version  : Herencia Simple

# Clase Base
class Empleado:

    def __init__(self, nombre, apellido):
        super().__init__()
        self.nombre = nombre
        self.apellido = apellido
        
    def nombre_completo(self):
        return self.nombre + " " + self.apellido

# Clase hija
class Desarrollador(Empleado):

    def __init__(self, nombre, apellido, especialidad):
        super().__init__(nombre, apellido)
        self.especialidad = especialidad

    def nombre_completo(self):
        return self.nombre.upper() \
                + " " + self.apellido.upper() 

emp_01 = Empleado("Juan","Acosta")
print(emp_01.nombre_completo())

des_01 = Desarrollador("Jaime","Gomez",
                "Programación en Python")
print(des_01.nombre_completo())
print(des_01.especialidad)

#'''

#''' Cuarta version  : Herencia Simple

# Clase Base
class Empleado:

    def __init__(self, nombre, apellido):
        super().__init__()
        self.nombre = nombre
        self.apellido = apellido
        
    def nombre_completo(self):
        return self.nombre + " " + self.apellido

# Clase hija
class Desarrollador(Empleado):
    
    def __init__(self, nombre, apellido, especialidad):
        super().__init__(nombre, apellido)
        self.especialidad = especialidad
        
    def nombre_completo_mayus_2(self):
        return super().nombre_completo().lower()

    def nombre_completo_mayus(self):
        return self.nombre_completo().lower()

    def nombre_completo(self):
        return self.nombre.upper() \
                + " " + self.apellido.upper() \
                + " : " + self.especialidad.upper()


def sum(a,b):
    return a+b

emp_01 = Empleado("Juan","Acosta")
print(emp_01.nombre_completo())

des_01 = Desarrollador("Jaime","Gomez",
        "Programación en Python")
print(des_01.nombre_completo())
print(des_01.nombre_completo_mayus())


'''
 Crear el atributo ciudad en la clase Empleado, 
 modificar el constructor en la clase Empleado.

 Modificar la clase Desarrollador para pasar el 
 valor del atributo ciudad a traves del 
 constructor de la clase Empleado

 Usar el atributo ciudad para ser usado en el
 metodo nombre_completo
'''


#'''


l = [1,2]
print(type(l))
l.append(3)

x = 1
print(type(x))


'''



'''




''' Quinta version  : Herencia Multiple

# Clase Base 1
class Empleado:

    def __init__(self, nombre, apellido):
        super().__init__()
        self.nombre = nombre
        self.apellido = apellido
        
    def nombre_completo(self):
        return self.nombre + " " + self.apellido

# Clase Base 2
class Investigador:

    def __init__(self, especialidad, anhos):
        super().__init__()
        self.especialidad = especialidad
        self.anhos = anhos
        
    def detalle_investigacion(self):
        det = "Especialida : " +  self.especialidad  \
                + " - " + " Anhos : " + str(self.anhos)
        return det

# Clase hija
class EmpleadoInvestigador(Empleado, Investigador):

    def __init__(self, nombre, apellido, especialidad, anhos):
       # Empleado.__init__(nombre, apellido)
       # Investigador.__init__(especialidad, anhos)
        pass

emp_01 = Empleado("Juan","Acosta")
print(emp_01.nombre_completo())

inv_01 = Investigador("Biotecnologia",13)
print(inv_01.detalle_investigacion())

#emp_inv_01 = EmpleadoInvestigador("Maribel","Alegria","Big Data",5)



#'''
