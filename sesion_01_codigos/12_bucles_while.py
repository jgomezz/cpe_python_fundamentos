'''
Curso : Programacion Basica de Python
Sesion : 01 
Tema : Introduccion a Python -  Bucles
Fecha : 08/02/202x
Author : Jaime Gomez

'''

#####################################
#     Loops : while
#####################################

print("------------------------")

''' 
Imprimir los numeros del 1 al 9 
'''

cont = 0
while cont < 5:
    cont +=1   # cont = cont + 1
    print(cont)


#####################################
#     Loops : while .. else
#####################################

print("------------------------")

''' 
Imprimir los numeros del 1 al 9 
y poner un mensaje al finalizar
'''

cont = 0
while cont < 9:
    cont +=1   # cont = cont + 1
    print(cont)
else :
    print("end cont = ", cont)


#####################################
#     Loops : while  break
#####################################

print("------------------------")

''' 
Imprimir los numeros del 1 al 9 
y cuando se llege al numero 4
detenga el proceso
'''

cont = 0
while cont < 9:
    cont +=1   # cont = cont + 1
    if  cont == 4 :
        print("break loop when cont = ", cont)
        break
    print(cont)
#else :
#    print("end cont = ", cont)

#####################################
#     Loops : while  break
#####################################

print("------------------------")

''' 
Imprimir los numeros del 1 al 9 
y no muestre los numeros 4 y 5
'''

cont = 0
while cont < 9:
    cont +=1   # cont = cont + 1
    if  cont == 4 or cont == 5 :
        print("continue loop")
        continue
    print(cont)
#else :
#    print("end cont = ", cont)


