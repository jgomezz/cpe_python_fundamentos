'''
Curso : Programacion Basica de Python
Sesion : 02 
Tema : Introduccion a Python -  Tuplas
Fecha : 15/02/202x
Author : Jaime Gomez

'''

#  index    0  1  2  3  4  5  6
mi_tupla = (10,20,30,40,50,60,70)

print(mi_tupla)
print("Primer elemento =",mi_tupla[0])
print("Ultimo elemento =",mi_tupla[-1])

#          -7 -6 -5 -4 -3 -2 -1        
#  index    0  1  2  3  4  5  6
mi_tupla = (10,20,30,40,50,60,70)

nro_elementos = len(mi_tupla)  #  
print("Nro. de elementos =",nro_elementos)
print("Ultimo elemento =",mi_tupla[nro_elementos-1])

# Con indices negativos
print("Primer elemento =",mi_tupla[-nro_elementos])

print("Ultimo elemento =",mi_tupla[-1])

#######################################
#              Slice
#
# [ start_index : stop_index : step ]
#######################################

#  index    0  1  2  3  4  5  6
mi_tupla = (10,20,30,40,50,60,70)

print("mi_tupla[1:4] =",mi_tupla[1:4])

print("mi_tupla[1:2:2] =",mi_tupla[1:2:2])
# (20,)
print("mi_tupla[1:6:2] =",mi_tupla[1:6:2])


#######################################
#    Operaciones de asignacion
#######################################

#  index    0  1  2  3  4  5  6
mi_tupla = (10,20,30,40,50,60,70)

'''
# Operaciones no permitidas en tuplas
mi_tupla[0] = 11
del(mi_tupla[0])
#'''

#######################################
#         Concatenacion de tuplas
#######################################

#  index      0  1  2  3
mi_tupla_1 = (10,20,30,40)
mi_tupla_2 = (100,200,300,400)

mi_tupla_f = mi_tupla_1 + mi_tupla_2
print(mi_tupla_f)

#######################################
#         Resta de tuplas
#######################################

mi_tupla_1 = (10,20,30,40)
mi_tupla_2 = (100,200,300,400)

'''
# Operaciones no permitidas en tuplas
mi_tupla_f = mi_tupla_1 - mi_tupla_2
print(mi_tupla_f)
#'''

#######################################
#     Multiplicacion de tuplas
#######################################

mi_tupla_1 = (10,20,30,40)
mi_tupla_tmp = mi_tupla_1 * 2
print(mi_tupla_tmp)

mi_patron = ("-*",)
print(type(mi_patron))
print(mi_patron)
mi_patron = mi_patron * 100
print(mi_patron)
print("".join(mi_patron))

#######################################
#     Division de tuplas
#######################################

mi_tupla_1 = (10,20,30,40)

'''
# Operaciones no permitidas en tuplas
mi_tupla_tmp = mi_tupla_1 / 4
print(mi_tupla_tmp)
#'''

#######################################
#  Recorrido de elementos de una tupla
#######################################

mi_tupla_1 = (10,20,30,40)
mi_tupla_1 = ("J","A","I","M","E",21,12.3,(2,3))

for elemento in mi_tupla_1:
    print(elemento)

'''
Ejercicio : En la tupla dada, 

mi_tupla = (10,20,30,40,50,60,70)

a) mostrar los valores :
  - (10,30,50)
  - (50,)
  - (40,50,60)
  - (60, 70)

b) recorrer la tupla usando un for
   y mostrar todos los valores a exception del 40 y 70

'''

#  index    0  1  2  3  4  5  6
mi_tupla = (10,20,30,40,50,60,70)
print("mi_tupla[0:3:2] =",mi_tupla[0:3:2])
print("mi_tupla[4] =",mi_tupla[4])
print("mi_tupla[3:4:1] =",mi_tupla[3:4:1])
print("mi_tupla[5:6] =" ,mi_tupla[5:6])

mi_tupla = (10,20,30,40,50,60,70)
print("mi_tupla =",mi_tupla[0:5:2])
print("mi_tupla =",mi_tupla[4])
print("mi_tupla =",mi_tupla[3:6:1])
print("mi_tupla =",mi_tupla[5:8:1])

mi_tupla = (10,20,30,40,50,60,70)
print(mi_tupla[5:7])

#######################################
#   Funciones Basicas
#######################################

mi_tupla_1 = (10,20,30,40)

maximo = max(mi_tupla_1)    
print(maximo)

minimo = min(mi_tupla_1)    
print(minimo)

suma = sum(mi_tupla_1)    
print(suma)


'''
  En la tupla

  mi_tupla_1 = (3,4,5,6,7,8,9,10,11,12,13)

  Calcular la suma de los números impares y la diferencia entre
  el mayor y el menor número impar
'''


mi_tupla = (3,4,5,6,7,8,9,10,11,12,13)
suma =0
for item in mi_tupla:
    if (item % 2) != 0:
        suma += item
print(suma)

mi_tupla_1 = (3,4,5,6,7,8,9,10,11,12,13)
suma = sum(mi_tupla_1[0:12:2])    
print(suma)

mi_tupla = (3,4,5,6,7,8,9,10,11,12,13)
nueva_tupla=(mi_tupla[0:11:2])
suma = sum(nueva_tupla)
print (suma)


#            0   1
mi_tupla = ("J","A","I","M","E",21,12.3,3)

tipo_var = type(mi_tupla[-1])

if tipo_var == str :
    print("Eres una cadena")

if tipo_var == int :
    print("Eres un entero")

mi_tupla = (1,20,3,4.5,2,"A",1.4,2,11.2)

# Calcular la suma de los numero enteros 
# y la suma de los decimales separados

# Solucion

# Si es entero es int
# Si es decimal es float

mi_tupla = (1,20,3,4.5,2,"A",1.4,2,11.2)

suma_ent = 0
suma_dec = 0

for elemento in mi_tupla:
    tipo_dato = type(elemento)
    #print(tipo_dato)
    if tipo_dato == int :
        suma_ent += elemento
        print("Eres una entero")
    elif tipo_dato == float :
        suma_dec += elemento
        print("Eres una decimal")
    else:
        print("Eres desconocido")

print(suma_ent)
print(suma_dec)



mi_tupla=(1,20,3,4.5,2,1.4,2,11.2)
suma_int=0
suma_float=0
for elemento in range(0,8):
    tipo_var=type(mi_tupla[elemento])
    #print(mi_tupla[elemento])
    #print(tipo_var)
    if tipo_var==int:
        suma_int += mi_tupla[elemento]
    elif tipo_var==float:
        suma_float += mi_tupla[elemento]
print(suma_int)
print(suma_float)

#
mi_tupla = (1,20,3,4.5,2,"A",1.4,2,11.2)
sum=0
su=0
n=len(mi_tupla)
for i in mi_tupla:
    if type(i)==int:
        sum+=i
    elif type(i)==float:
        su+=i
    else:
        print("es una cadena")
print("suma enteros = ",sum,"suma decimales = ",su)

#
mi_tupla = (1,20,3,4.5,2,"A",1.4,2,11.2)
suma_enteros=0
suma_decimales=0
for dato in mi_tupla:
    tipo_var=type(dato)
    print(tipo_var)
    if tipo_var==int:
        suma_enteros=suma_enteros+dato
    elif tipo_var== float:
        suma_decimales=suma_decimales+dato
print("la suma de los numeros enteros es: ", suma_enteros)
print("la suma de los numeros decimales es: ", suma_decimales)


#######################################
#   Ejercicio
#######################################

'''
Elabore un programa en Python que calcule 
el promedio de 5 números. Emplee listas.

   mi_tupla_1 = (10,20,30,40,50)

'''

mi_tupla_1 = (10,20,30,40)
st = sum(mi_tupla_1)    
l  = len(mi_tupla_1)

prom = st / l
prom = round(prom, 2) # funcion para redondear

print("El promedio = ", prom)
