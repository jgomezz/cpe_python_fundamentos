'''
Curso : Programacion Basica de Python
Sesion : 01 
Tema : Introduccion a Python -  Bucles
Fecha : 08/02/2020
Author : Jaime Gomez

'''
#####################################
#     Bucles : for  range
#####################################

'''
La funcion range(max) devuelve 
valores enteros 0 y max-1
'''

print(range(21))




for i in range(4):
    print("Hola mundo ..!")



for i in range(4):
    print("Hola mundo ..! ",i)

exit(-1)

'''
La funcion range(min, max) devuelve 
valores enteros entre min y max-1
'''

for i in range(1,4):
    print(i)


'''
La funcion range(min, max, step) devuelve 
valores enteros entre min y max-1, 
incrementados de step en step
'''    
#        step = 2
# min                 max               
# 2, 4, 6, 8, 10 , 12 , 13 , 14

for valor in range(2,14,2) :
    print(valor)


# 0, 2, 4, 6, 8, 10, 12
for valor in range(0,13,2) :
    print(valor)

# 0,1,2,3,4,5,6
for valor in range(7) :
    print(valor)



for i in range(0,4,2):
    print("secuencia :",i)

# Imprimir el cuadrado de los
# 5 numeros impares, usa range()

for i in range(1,11,2):
    print(i**2)

for i in range(0,9,2):
    print(">>",i)
    print((i+1)*(i+1))


#####################################
#     Bucles : for
#####################################
#nombre = ["J","a","i","m","e"]
nombre = "Jaime"

for c in nombre:
    print(c)

notas = [13, 14, 12, 18]
for n in notas:
    print(n)

'''
For para modificar valores del listado
'''
# Forma 1

notas = [13, 14, 12, 18]
print(notas)

for i in range(len(notas)):
    print("indice =", i, " & valor =", notas[i])
    notas[i] = 10 

print(notas)

# Forma 2

notas = [13, 14, 12, 18]
print(notas)

for i, nota in enumerate(notas):
    print("indice =", i, " & valor =", nota)
    notas[i] = 10

print(notas)

# break 
for j in range(3):
    print("master =",j)
    for i in range(100):
        print("slave =",i)
        if i == 5: break # exit()



notas = [13, 14, 12, 18]

print(sum(notas))
print(min(notas))  
print(max(notas))

'''
Dado notas
   notas = [13, 14, 12, 18]
Calcular el valor min de un 
elemento usando for
'''


# Solucion 1

notas = [13, 14, 12, 18]

min_nota = 20 # nota mayor
for nota in notas:
    if nota < min_nota:
        min_nota = nota

print(min_nota)

# Solucion 2 , falta mejorar
notas = [16, 14, 12, 18]
for n in range(len(notas)):
    aux=0
    if notas[n]<notas[n+1]:
        aux=notas[n]
print('El minimo es: ',aux)


'''
range
'''




'''
En el arreglo anterior, solo imprimir 
las notas mayores a 13
'''
print("------------------------")
notas = [13, 14, 12, 18]
for n in notas:
    if n > 13 :
        print(n)

