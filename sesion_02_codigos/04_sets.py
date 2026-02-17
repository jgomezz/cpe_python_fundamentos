'''
Curso : Programacion Basica de Python
Sesion : 02 
Tema : Introduccion a Python -  Sets
Fecha : 15/02/202x
Author : Jaime Gomez

'''

print("--------------------------------------")


colourSet  = {"red", "green", "yellow", 
              "blue", "blue", "blue"}

# No se repite
print("colourSet     :",  colourSet)



colourList = ["red", "green", "yellow", "blue",
              "blue", "blue"]

print("colourList    :",  colourList)


print("--------------------------------------")

colours = {"red", "green", "yellow", "blue"}
print("colours                :",  colours)
print("len(colours)           :",  len(colours))
print("type(colours)          :",  type(colours))

colours.add("white")
print("colours  1             :",  colours)

colours.add("white")
print("colours   2            :",  colours)

colours.remove("green")
print("colours                :",  colours)


print("--------------------------------------")

ratings = {0,3,4,19,5,6,7,8}
print("ratings       :", ratings)
print("min(ratings)  :", min(ratings))
print("max(ratings)  :", max(ratings))
print("sum(ratings)  :", sum(ratings))

print("--------------------------------------")

list1 = {"Panam Sports", 28.07, 2019}
list2 = list1.copy()
print("list1 :", list1)
print("list2 :", list2)

print("--------------------------------------")

colours1 = {"red", "green", "yellow", "blue"}
colours2 = {"white", "black", "purple"}

#colours1 = colours1 + colours2
colours1.update(colours2)
print("colours1 :", colours1)


print("--------------------------------------")

sports = ("Soccer","Tennis","Baseball","Squash")
existShotting = "Shotting" in sports
print("sports          :", sports)
print("existShotting   :", existShotting)
existSoccer = "Soccer" in sports
print("existSoccer     :", existSoccer)

print("--------------------------------------")

sports = {"Soccer","Tennis","Baseball","Squash"}

for value in sports:
    print(value)

print("--------------------------------------")

sports = {"Soccer","Tennis","Baseball","Squash"}
print("sports                   :", sports)

sports = tuple(sports)
print("tuple(sports)            :", sports)

sports = list(sports)
print("list(sports)             :", sports)

sports = set(sports)
print("set(sports)              :", sports)

s = "10"
s = int(s)

'''
En la lista siguiente 

lista = ["Juan", "Jose", "Pedro", "Pedro", "Jose"]

Obtener solo los nombres no repetidos.

'''
lista = ["Juan", "Jose", "Pedro", "Pedro", "Jose"]
lista2=set(lista)
print(lista2)