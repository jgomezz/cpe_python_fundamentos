'''
Curso : Programacion Basica de Python
Sesion : 02 
Tema : Introduccion a Python -  String
Fecha : 15/02/2020
Author : Jaime Gomez

'''
###############################
#         String
###############################

#      0123456789012345
msg = 'Mi nuevo mensaje'
print(msg)

print("Primer caracter :",msg[0])
print("Ultimo caracter :",msg[15])
print("Primer caracter :",msg[-16])
print("Ultimo caracter :",msg[-1])
print("Numero de caracteres :", len(msg))

#            -2 -1
#         0123456
patron = "Curso-X"

print(patron[6])
print(patron[-1])

nuevo_mensaje = "Python es un lenguaje"

print(nuevo_mensaje[0])

size = len(nuevo_mensaje)
print(nuevo_mensaje[size-1])

print(nuevo_mensaje[-1])


#######################################
#              Slice
#
# [ start_index : stop_index : step ]
#######################################

msg = "Mi nuevo mensaje"

print("msg[3:8:1] :",msg[3:8:1])
print("msg[3:11:3] :",msg[3:11:3])
print("msg[-3:-11:-3] :",msg[-3:-11:-3])

###############################
#       Basic Function
###############################

msg = 'Mi nuevo mensaje'

print(msg)
print(msg.upper())

print(msg)
print(msg.lower())

print(msg)
# Convierte Mayuscula a Minuscula
# y Minusculas a Mayusculas
print(msg.swapcase())

msg = 'mi nuevo mensaje'
print(msg)
print(msg.capitalize())

'''
nombres = ["Jose","Juan","pedro"]

Convertir Jose a jose

Convertir Juan a JUAN

Convertir  pedro a Pedro
'''
#            0       1      2
nombres = ["Jose","Juan","pedro"]

print(nombres[0].lower())  # Jose


nombre = ["Jose","Juan","pedro"]
print(nombre)
print(nombre[0].lower())
print(nombre)
print(nombre[1].upper())
print(nombre)
print(nombre[2].capitalize())

nombres = ["Jose","Juan","pedro"]
print("jose:",nombres[0].lower())
print("JUAN:",nombres[1].upper())
print("Pedro:",nombres[2].capitalize())

nombres=["Jose","Juan","pedro"]
print(nombres[0].lower())
print(nombres[1].upper())
print(nombres[2].capitalize())

nombres= ["Jose","Juan","pedro"]
print(nombres[0])
print(nombres[0].lower())


###############################
#     Advanced Function
###############################
       
msg = 'Mi nuevo mensaje'

# Find
# From the first position
print(msg.find("nue"))

# Return -1 if dont exist the string
print(msg.find("abc"))

print(msg.find("e"))

# From the last position
print(msg.rfind("e"))

# in

msg = 'Mi nuevo mensaje'

exp = "Mi" in msg
print(exp)

exp = "abc" in msg
print(exp)

participantes_en_fiesta = "Jaime Pedro Alicia"
invitado = "Miguel"
participo =  invitado in participantes_en_fiesta
participo =  "Eduardo" in participantes_en_fiesta

participantes_en_fiesta = ["Jaime", "Pedro", "Alicia"]
invitado = "Alicia"
participo =  invitado in participantes_en_fiesta
print(participo)

# Count
msg = 'Mi nuevo mensaje'
print(msg.count("e"))

# Replace
msg = 'Mi nuevo mensaje'
print(msg.replace(" ","_"))
print(msg)

###############################
#     Matematic Operation
###############################

# Suma
msg = 'Mi nuevo mensaje'
msg_1 = " es "
msg_2 = "Python"
msg = msg + msg_1 + msg_2
print(msg)

# Multiplicacion
msg = 'Mi nuevo mensaje '
msg = 2 * msg
print(msg)

msg = 'Mi nuevo mensaje '
msg = msg * 2
print(msg)


lista_nro = [1,2,3,4,5,6]

suma = 0 ;
for n in lista_nro:
    suma = suma + n
#                            (mod)
# ciclo     suma      n      suma      
#    1        0       1        1
#    2        1       2        3 


for n in range(10):
    dato =  input("ingresar valor")    


nombres = ["Jaime", "Pedro", "Alicia"]

for n in range(len(nombres)):
    print(n) # 0, 1, 2

for n in nombres:
    print(n) # "Jaime", "Pedro", "Alicia"

'''
mensaje : "Hoy es miercoles, y la clase Empieza de 7 a 9:30 pm"

- Contar cuantas veces se usa la letra e 
- Reemplazar pm por PM
- Longitud de la cadena
- Convertir todo a Mayúscula

'''



