'''
Curso : Programacion Basica de Python
Sesion : 02 
Tema : Introduccion a Python -  Archivos
Fecha : 25/05/202x
Author : Jaime Gomez

'''
# lectura
archivo = open("sesion02/08_datos.txt")

for linea in archivo:
    print(linea)

archivo.close()    

# Escritura : crea el nuevo archivo  
archivo = open("sesion02/08_datos_tmp.txt","w")

archivo.write("Linea tres \n")

archivo.close()    

# Escritura : adiciona  
archivo = open("sesion02/08_datos_adicional.txt","a")

archivo.write("Linea dos \n")

archivo.close()    