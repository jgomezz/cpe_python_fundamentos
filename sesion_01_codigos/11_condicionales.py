'''
Curso : Programacion Basica de Python
Sesion : 01 
Tema : Introduccion a Python - Condicionales
Fecha : 20/02/2026
Author : Jaime Gomez
Version : 1.2

'''

#####################################
#     Condicional : if
#####################################
'''
 Para que un estudiante pase un curso , 
 debe aprobar con la nota minima de 11. 
 , si aprueba se le envia su constancia
 virtual de aprobacion.
'''

'''

NOTA_MINIMA = 11

nota_final  = 18 # nota final

if nota_final >= NOTA_MINIMA:
    print("Envio de constancia virtual de aprobacion")

#'''

#####################################
#     Condicional : if ... else
#####################################
'''
 Para que un estudiante pase un curso , 
 debe aprobar con la nota minima de 11. 
 , si aprueba se le envia su constancia
 virtual de aprobacion. Si el estudiante 
 no aprueba solo se le envia su nota final.
'''

'''

NOTA_MINIMA = 11

nota_final_estudiante  = 19 # nota final

if nota_final_estudiante >= NOTA_MINIMA :
    print("Envio de constancia virtual")
else :
    print("Envio de promedio final")

#'''


#####################################
#  Condicional : if .. elif .. else
#####################################
'''
 El estudiante aprueba con una nota mayor o igual a 11, 
 en este caso se le envia su constancia virtual. En caso el 
 estudiante tenga una nota entre 10 ( inclusive el 10) y 
 menor  a 11, se le tomara una examen adicional, si el estudiante 
 tiene una nota menor a 10 solo se le envia su nota final.
'''

#'''
NOTA_MINIMA_APROB = 11
NOTA_MINIMA_RECUP = 10

nota_final  = 9.50 # nota final

if nota_final >= NOTA_MINIMA_APROB :
    print("Envio de constancia virtual")
elif NOTA_MINIMA_RECUP <= nota_final < NOTA_MINIMA_APROB :
    print("Se le toma examen de recuperacion")
else:
    print("Envio de promedio final")    


if nota_final >= NOTA_MINIMA_APROB :
    print("Envio de constancia virtual")
elif nota_final < NOTA_MINIMA_APROB and nota_final >= NOTA_MINIMA_RECUP :
    print("Se le toma examen de recuperacion")
else:
    print("Envio de promedio final")   



#'''


'''
# Conditional expression

res =  "Jaime " if False else "Jose"
print( res)

res =  "Jaime " if True else "Jose"
print( res)


# Pass : To end an block
if True :
    pass

'''