'''
Curso : Programacion Basica de Python
Sesion : 03
Tema : Introduccion a Python -  Metodo estatico y Metodo de clase
Fecha : 22/02/2020
Author : Jaime Gomez

'''

'''
Para debug en mac : export LC_ALL=C
'''

''' Primera version  : Metodo de clase
class Empleado:

    aumento  = 1.10
    nro_empleados = 0

    def __init__(self, nombre, apellido, sueldo):
        super().__init__()
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo
        Empleado.nro_empleados += 1

    def nombre_completo(self):
        return self.nombre + " " + self.apellido

    def incremento_sueldo(self):
        self.sueldo = \
            int(self.sueldo * self.aumento)

    # Metodo de una clase
    @classmethod
    def modificar_aumento(cls, x):
        cls.aumento = x

emp_01 = Empleado("Jaime","Gomez",1000)
emp_02 = Empleado("Oscar","Garcia",2000)

# En estos 3 casos se modifica el 
# atributo de clase
Empleado.modificar_aumento(1.05)
emp_01.modificar_aumento(1.05)
emp_02.modificar_aumento(1.05)

#Empleado.aumento=1.50
#emp_01.aumento=1.50
#emp_02.aumento=1.50

print(emp_01.aumento)
print(emp_02.aumento)
print(Empleado.aumento)

# Crear una metodo de clase para cambiar 
# el valor de la variable de clase descuento


#'''

''' Segunda version  : Metodo de clase
class Empleado:

    aumento  = 1.10
    nro_empleados = 0

    def __init__(self, nombre, apellido, sueldo):
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo
        Empleado.nro_empleados += 1

    def nombre_completo(self):
        return self.nombre + " " + self.apellido

    def incremento_sueldo(self):
        self.sueldo = int(self.sueldo * self.aumento)

    @classmethod
    def modificar_aumento(cls, aumento):
        cls.aumento = aumento

    @classmethod
    def construir_desde_str(cls, str_emp):
        nombre, apellido, sueldo =  str_emp.split(",")
        return cls(nombre, apellido, sueldo)

# crear un atributo de titulo
str_emp_01 = "Jaime,Gomez,Ingeniero,1000"
nombre, apellido, sueldo =  str_emp_01.split(",")
emp_01 = Empleado(nombre, apellido, sueldo)

print(emp_01.nombre)
print(emp_01.apellido)
print(emp_01.sueldo)

str_emp_01 = "Jaime,Gomez,1000"
emp_01 = Empleado.construir_desde_str(str_emp_01)

print(emp_01.nombre)
print(emp_01.apellido)
print(emp_01.sueldo)

#'''

''' Tercera version  : Metodo estaticos
class Empleado:

    aumento  = 1.10
    nro_empleados = 0

    def __init__(self, nombre, apellido, sueldo):
        super().__init__()
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo
        Empleado.nro_empleados += 1

    def nombre_completo(self):
        return self.nombre + " " + self.apellido

    def incremento_sueldo(self):
        self.sueldo = int(self.sueldo * self.aumento)

    @classmethod
    def modificar_aumento(cls, aumento):
        cls.aumento = aumento

    @classmethod
    def construir_desde_str(cls, str_emp):
        nombre, apellido, sueldo =  str_emp.split(",")
        return cls(nombre, apellido, int(sueldo))

    @staticmethod
    def es_buen_sueldo(sueldo):
        if sueldo >= 10000:
            return True
        return False    


str_emp_01 = "Jaime,Gomez,50000"
emp_01 = Empleado.construir_desde_str(str_emp_01)
print(emp_01.es_buen_sueldo(emp_01.sueldo))

#'''