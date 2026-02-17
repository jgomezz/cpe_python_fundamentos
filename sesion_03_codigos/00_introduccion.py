'''
Curso : Programacion Basica de Python
Sesion : 03
Tema : Introduccion a Python -  Introduccion a clases
Fecha : 01/06/202x
Author : Jaime Gomez

'''

# int, float and boolean : atomic objects
# string, tuples, set and dictionary : no atomic objects

mi_dato = 1 
print(type(mi_dato))

# Characteristics and Behaviors 

#               Object
# -----------------------------------------

#
# An object type is defined by two things: a set 
# of properties and a set of behaviors.
#
# Object type properties are data that define your object
# Object type behaviors are operations that define your object


numbers = [1,2,3,4,5,6]

for n in numbers : print(n)

for n in numbers[::-1] : print(n)

for n in numbers.reverse() : print(n)


# Definición de una clase
class Name_class:

    # Definición de una atributo de clase
    at_class  =  1 

    # Definición de constructor
    def __init__(self):
        # Define un atributo
        self.at_obj = None

    # Definición de un método
    def name_method(self):
        print("do something")