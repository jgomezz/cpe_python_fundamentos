'''
Curso : Programacion Basica de Python
Sesion : 04
Tema : Introduccion a Python -  Conexion a BBDD
Fecha : 29/02/202x
Author : Jaime Gomez
'''

# Importando librerias
import mysql.connector

'''
# Mostrar esquemas de base de datos
config =  {"host":"localhost", 
           "user":"root", 
           "password":""}

conn = mysql.connector.connect(**config)

cur = conn.cursor()

sql = "SHOW DATABASES"  # input

cur.execute(sql)

# output cur
print(type(cur))

for line in cur:
    print(type(line)) 
    print(line)

# Cerrar conexion
conn.close()

#'''

'''
# Crear esquema de base de datos

config =  {"host":"localhost", 
           "user":"root", 
           "password":""}

conn = mysql.connector.connect(**config)
cur = conn.cursor()
sql = "CREATE DATABASE hr6"
cur.execute(sql)
conn.close()

#'''

#'''
# Verifica que esquema de base de datos exista

config =  {"host":"localhost", 
           "user":"root", 
           "password":"", 
           "db":"hr6"}

conn = mysql.connector.connect(**config)
print(conn)
conn.close()

#'''

