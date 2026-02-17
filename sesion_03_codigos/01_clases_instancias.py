'''
Curso : Programacion Basica de Python
Sesion : 03
Tema : Introduccion a Python -  Clases e Instancias
Fecha : 22/02/2020
Author : Jaime Gomez

'''

'''
Para debug en mac : export LC_ALL=C
'''

''' Primera version
# Define una clase
class Empleado:
    pass

emp_01 = Empleado() # Se instancia una clase
emp_02 = Empleado()

print(emp_01)
print(emp_02)

emp_01.nombre = "Jaime"
emp_01.apellido = "Gomez"

print(emp_01.nombre)
print(emp_01.apellido)

emp_01.apellido = "Garcia"

print(emp_01.nombre)
print(emp_01.apellido)

# Crear el atributo DNI en emp_01 y darle un valor
# Crear los atributos nombre, apellido 
# y DNI en emp_02 , darle valores

emp_01.dni = "12345678"
print(emp_01.dni)

emp_02.nombre = "Juan"
emp_02.apellido = "Acosta"
emp_02.dni = "5652553"
print(emp_02.nombre)
print(emp_02.apellido)
print(emp_02.dni)

#'''


''' Segunda version
class Empleado:

    # Se define el constructor    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def nombre_completo(self):
        return self.nombre + " " + self.apellido

#emp_01 = Empleado()
emp_01 = Empleado("Jaime","Gomez")

print(emp_01.nombre)
print(emp_01.apellido)
print(emp_01.nombre_completo())

emp_01.apellido = "Garcia"

print(emp_01.nombre)
print(emp_01.apellido)
print(emp_01.nombre_completo())

# Agregar el atributo dni a la clase Empleado y
# le pasas un valor al instanciar la clase

'''

#''' Tercera version
class Empleado:
    
    def __init__(self, nombre, apellido):
        #super().__init__()
        self.nombre = nombre
        self.apellido = apellido

    def nombre_completo(self):
        return self.nombre + " " + self.apellido

emp_01 = Empleado("Jaime","Gomez")

print(emp_01.nombre_completo())
print(Empleado.nombre_completo(emp_01))
print(type(emp_01))
#'''
