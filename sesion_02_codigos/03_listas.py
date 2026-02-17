'''
Curso : Programacion Basica de Python
Sesion : 02 
Tema : Introduccion a Python -  Listas
Fecha : 15/02/2020
Author : Jaime Gomez

'''

#  index    0  1  2  3  4  5  6
mi_lista = [10,20,30,40,50,60,70]
print(type(mi_lista))

print(mi_lista)
print("Primer elemento =",mi_lista[0])

# index    0  1  2  3  4  5  6
mi_lista = [10,20,30,40,50,60,70]

# 
nro_elementos = len(mi_lista)  #  
print("Nro. de elementos =",nro_elementos)
print("Ultimo elemento =",mi_lista[nro_elementos-1])

# Con indices negativos
print("Primer elemento =",mi_lista[-nro_elementos])
print("Ultimo elemento =",mi_lista[-1])

#######################################
#              Slice
#
# [ start_index : stop_index : step ]
#######################################

#  index    0  1  2  3  4  5  6
mi_lista = [10,20,30,40,50,60,70]

print("10, 30, 50 =",mi_lista[0:6:2])

print("30, 60 =",mi_lista[2:6:3])

print("mi_lista[1:4] =",mi_lista[1:4])

print("mi_lista[1:2:2] =",mi_lista[1:2:2])

print("mi_lista[1:6:2] =",mi_lista[1:6:2])



#######################################
#    Operaciones de asignacion
#######################################

mi_lista = [10,20,30,40,50,60,70]
print("lista inicial", mi_lista)
mi_lista[0] = 11
print("lista modificada", mi_lista)


#######################################
#         Concatenacion de listas
#######################################

print("-----------------------------")
#  index    0   1  2  3
mi_lista_1 = [10,20,30,40]
mi_lista_2 = [100,200,300,400]

mi_lista_f = mi_lista_1 + mi_lista_2
print(mi_lista_f)


#######################################
#         Resta de listas
#######################################

mi_lista_1 = [10,20,30,40]
mi_lista_2 = [100,200,300,400]

'''
# Operaciones no permitidas en listas
mi_lista_f = mi_lista_1 - mi_lista_2
print(mi_lista_f)
'''

#######################################
#     Multiplicacion de lista
#######################################

mi_lista_1 = [10,20,30,40]
mi_lista_tmp = mi_lista_1 * 4
print(mi_lista_tmp)

#######################################
#     Division de listas
#######################################


mi_lista_1 = [10,20,30,40]

'''
# Operaciones no permitidas en tuplas
mi_lista_tmp = mi_lista_1 / 4
print(mi_lista_tmp)
'''

#######################################
#  Recorrido de elementos de una lista
#######################################

mi_lista_1 = [10,20,30,40]

for elemento in mi_lista_1:
    print(elemento)

#                   
mi_lista_1 = [10,20,"J",40,50,"A",70,"I",90]

# Dado una lista, unificar los caracteres
# en una sola cadena



mi_lista_1 = [10,20,"J",40,50,"A",70,"I",90]
concat=" "
for dato in mi_lista_1:
    tipo_var=type(dato)
    #print(tipo_var)
    if tipo_var==str:
        concat += dato
print(concat)

'''
Ejercicio : Dado la lista
mi_lista_2 = [10,20.5,"P",40.4,50,"E",70.8,"R",90,"U"]
realizar lo siguiente :
 - Calcular la suma de los números enteros
 - Calcular la suma de los números decimales
 - Concatenar las letras

'''



#######################################
#   Funciones Basicas
#######################################

mi_lista_1 = [10,20,30,40]

maximo = max(mi_lista_1)    
print(maximo)

minimo = min(mi_lista_1)    
print(minimo)

suma = sum(mi_lista_1)    
print(suma)


#           0  1  2  3  4  5  6  7  8 
mi_lista = [20,20,20,30,40,40,40,50,60]

print(len(mi_lista))

# Cuenta cuantas veces se repite un dato
print(mi_lista.count(20))

print(mi_lista.count(40))

print(mi_lista.index(20))

print(mi_lista.index(40,1,8))

#print(mi_lista.index(2000))

#######################################
#   append, extend, insert, del y pop
#######################################

# Operacion append() 
list1 = ["Panam Sports", 28.07, 2019]
print("list1           : ", list1)

list2 = ["Rugby", 11]
list1.append(list2)
print("list1           : ", list1)

# operation extend()
list1 = ["Panam Sports", 28.07, 2019]
print("list1           : ", list1)

list2 = ["Rugby", 11]
list1.extend(list2)
print("list1           : ", list1)

# operation insert()
list1 = ["Panam Sports", 28.07, 2019]
print("list1           : ", list1)

pos = 1
valor = "Nuevo"
list1.insert(pos, valor)
print("list1           : ", list1)

# operacion del() 
list1 = ["Panam Sports", 28.07, 2019]
print("list1    : ", list1)
print("list1[0] : ", list1[0])
del(list1[0])
print("list1    : ", list1)


##   
##     .....   P4  P3  P2   P1   <= Cashier
##

# operacion pop()  
list1 = ["Panam Sports", 28.07, 2019]
print("list1    : ", list1)

valor = list1.pop()
print("valor    : ", valor)
print("list1    : ", list1)

valor = list1.pop()
print("valor    : ", valor)
print("list1    : ", list1)

### append()   pop() : Permiten implementar Pilas :Stacks
 
listado_alumnos = ["Jose","Pedro","Maria"]

# Agregar al final de la lista
#  "Eduardo" , "Maribel" y "Juan"
listado_alumnos.append("Eduardo")
listado_alumnos.append("Maribel")
listado_alumnos.append("Juan")
print(listado_alumnos)

# Retirar los 2 últimos nombres ingresados
# e imprimirlos por consola

nombre = listado_alumnos.pop()
print(nombre)
print(listado_alumnos)

nombre = listado_alumnos.pop()
print(nombre)
print(listado_alumnos)


'''
Ejercicio 2-2 : Dado la lista
mi_lista_2 = [10,20.5,"P",40.4,50,"E",70.8,"R",90,"U"]
realizar lo siguiente :
 - Crear una lista con números enteros y obtener el mayor , 
   el menor valor y la cantidad de elementos
 - Crear una lista con números decimales y obtener el mayor, 
   el menor valor y la cantidad de elementos

'''


#######################################
#  Funciones avanzadas   
#######################################


# operacion reverse()
mi_lista = [10,20,30,40,50,60,70,80,90]
print(mi_lista)

mi_lista.reverse() # invierte lista
print(mi_lista)

# operacion sort()
mi_lista = [10,20,80,30,70,90,40,50,60]
print(mi_lista)

mi_lista.sort(reverse=True) # ordena lista
print(mi_lista)

# operacion split()
frase = "Mi nuevo mensaje"

# Separados por " "
palabras = frase.split(" ") 
print(palabras)

# operacion join()
palabras = ['Mi', 'nuevo', 'mensaje']

# Separados por " "
frase = " ".join(palabras)
print(frase)

'''
Elabore un programa en Python que calcule 
el promedio de 5 numeros. Emplee listas.

   mi_lista_1 = (10,20,30,40,50)

'''

mi_lista_1 = (10,20,30,40,50)

promedio = sum(mi_lista_1)/len(mi_lista_1)

promedio = round(promedio, 2)

print(promedio)

'''
Elabore un programa en Python que calcule 
el promedio de 5 numeros. Emplee listas.

   mi_lista_1 = (10,20,30,40,50)

'''

mi_lista_1 = (10,20,30,40,50,7)
st = sum(mi_lista_1)    
l  = len(mi_lista_1)

prom = st / l
prom = round(prom, 2) # funcion para redondear

print("El promedio = ", prom)

'''
Python 3.8
Visual Studio Code

'''


'''

  practica_01_Jaime_Gomez.py

  Dado una listas

    A = [10, 12, 13, 14, 15]

  Crear una funcion 

    mi, ma, pr , su , ln = estadistica(A)

    mi : valor minimo
    ma : valor maximo
    pr : promedio
    su : suma total
    ln : nro. de elementos

'''

mi_lista_3 = ["Jaime", "Jaime", True]

print(mi_lista_3[0])
print(mi_lista_3[1])
print(mi_lista_3[2])

#                                      0  1
mi_lista_4 = ["Jaime", "Gomez", True, [12,13]]
#                0      1        2      3

print(mi_lista_4[3][1])

x = ["Jaime", "Jaime", True]
print(set(x))
x = {"Jaime", "Jaime", True}
print(x)