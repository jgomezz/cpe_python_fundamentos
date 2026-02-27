'''
Curso : Programacion Basica de Python
Sesion : 02 
Tema : Introduccion a Python -  Sets
Fecha : 15/02/202x
Author : Jaime Gomez

'''


'''
1ra pregunta
'''
color = ["Azul","Rojo", "Verde", "Blanco", "Blanco"]
print(color)
'''
2da pregunta
'''
color = {"Azul","Rojo", "Verde", "Blanco"}
print(color)

'''
3ra pregunta
'''
color = {"Azul","Rojo", "Verde", "Blanco", "Blanco"}
print(color)

print("------------ SALON DE CLASES --------------------------")

participantes = ["Jaime", "Maria", "Pedro", "Jaime", "Maria", "Juan","Juan", "Ana", "Ana", "Ana"]
print(participantes)

nombres_unico = set(participantes)
print(nombres_unico)

for nombre in nombres_unico:
    print(f"El nombre {nombre} aparece {participantes.count(nombre)} veces en la lista")








