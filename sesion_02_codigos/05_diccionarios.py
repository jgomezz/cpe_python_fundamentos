'''
Curso : Programacion Basica de Python
Sesion : 02 
Tema : Introduccion a Python -  Diccionarios
Fecha : 22/02/202x
Author : Jaime Gomez

'''
'''
mi_identidad = {
    "nombre" : "Jaime",
    "apellido" : "Gomez",
    "telefono" : 999999,
    123      : "12334",
    "estudios" : { "superior" :"UNI",
                   "secundaria": "Perú Birf",
                   "primaria" : "6032"}
}
print(mi_identidad["estudios"]["primaria"])
print(mi_identidad[123])
'''


                   # llave : valor ,
campeones_futbol = {"2022":"Argentina",
                    "2018":"Francia",
                    "2014":"Alemania",
                    "2010":"Holanda",  # "2010":"España",
                    "2006":"Italia"}

# Tamanho
l = len(campeones_futbol)
print(l)   

# Lectura
print(campeones_futbol["2010"])   

# Modificacion
campeones_futbol["2010"] = "España"
print(campeones_futbol["2010"])   

print(campeones_futbol)

# Insertar o Agregar
campeones_futbol["2002"] = "Brasil"
print(campeones_futbol)

campeones_futbol["1998"] = "Francia"
print(campeones_futbol)

# Eliminar
campeon_2002 = campeones_futbol.pop("2002")
print(campeon_2002)
print(campeones_futbol)

campeon_2014 = campeones_futbol.pop("2014")
print(campeon_2014)
print(campeones_futbol)

#######################################
#  Llaves y valor de los diccionarios  
#######################################

                   # llave : valor ,
campeones_futbol = {"2018":"Francia",
                    "2014":"Alemania",
                    "2010":"España",
                    "2006":"Italia"}

# Llaves
print(campeones_futbol.keys())

for key in campeones_futbol.keys():
    print(key)

# Valores
print(campeones_futbol.values())

for value in campeones_futbol.values():
    print(value)

# Elementos
print(campeones_futbol.items())

for key,value in campeones_futbol.items():
    print(key, ":",value)



#######################################
#  not in , in 
#######################################

                   # llave : valor ,
campeones_futbol = {"2018":"Francia",
                    "2014":"Alemania",
                    "2010":"España",
                    "2006":"Italia"}

'''
Declarame los dias de la semana

01 --> Lunes
07 --> Domingo

'''


'''
Dado el siguiente diccionario, convertir
las primeras letras de cada dia de la semana
en mayuscula
'''
dias_de_la_semana={ "01":"lunes",
                    "02":"Martes",
                    "03":"Miercoles",
                    "04":"Jueves",
                    "05":"viernes",
                    "06":"Sabado",
                    "07":"domingo"}

msg = "hola"
msg = msg.capitalize()
print(msg)

for key,value in dias_de_la_semana.items():
    print(key, ":",value)

dias_de_la_semana={ "01":"lunes",
                    "02":"Martes",
                    "03":"Miercoles",
                    "04":"Jueves",
                    "05":"viernes",
                    "06":"Sabado",
                    "07":"domingo"}

# Solucion 1
for dia in dias_de_la_semana.keys():
    print(dia)  #  dia es la llave
    valor = dias_de_la_semana[dia] # obtener el valor
    dias_de_la_semana[dia]=valor.capitalize()
    print(dias_de_la_semana[dia])

# Solucion 2
for key, value in dias_de_la_semana.items():
    dias_de_la_semana[key]=value.capitalize()
   

print(dias_de_la_semana)


'''
?? 
'''
dias_semanas = {0:"Lunes",
                1:"Martes",
                2:"Miercoles",
                3: "Jueves",
                4:"Viernes",
                5:"Sabado,",
                6:"Domingo"}

dias_semanas = ["Lunes","Martes"]

print(dias_semanas[0])




print( "2018" in campeones_futbol)

print( "2018" not in campeones_futbol)


#######################################
#  Ejercicios  Propuesto 
#######################################

'''
 Contar cuantas veces las palabras se repiten, 
 no distinguir entre minusculas y mayusculas
'''
paragrafo \
    = "Python eS un lenguaje SENCILLO DE programacion que Es sencillo de aprender"

# Solucion
palabras = paragrafo.split(" ")
contador = {}

for palabra in palabras:
    palabra = palabra.lower()
    if palabra not in contador:
        contador[palabra] = 1
    else:
        contador[palabra] += 1

print(contador)

#######################################
#  Ejercicios  
#######################################

alumnos_python = {"1000001":("Jaime","Gomez"),
                  "1000002":("Jose","Velasque"),
                  "1000003":("Maria","Alegria") }

print(alumnos_python["1000001"])   
print(alumnos_python["1000002"])   
print(alumnos_python["1000003"])   

pbi_peru = {2016:195.7,
            2017:214.3,
            2018:225.3,
            2019:230.4,
            2020:202.7,
            2021:225.9}
'''

Ejercicio : Calcular el promedio del PBI de los años 2016, 2018 y 2020

'''




print(pbi_peru[2016])

'''
# En que año superamos los 200
for (llave,valor) in pbi_peru.items():
    #print(llave, " -->", valor)
    if valor > 200 :
        print(llave, " -->", valor)
        break  # sale del bucle
'''

# En que año superamos los 200
flag = True # Bandera
for (llave,valor) in pbi_peru.items():
    #print(llave, " -->", valor)
    if valor > 200 and  flag :
        print(llave, " -->", valor)
        flag = False 
