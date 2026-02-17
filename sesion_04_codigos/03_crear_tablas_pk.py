'''
Curso : Programacion Basica de Python
Sesion : 04
Tema : Introduccion a Python -  Crear Tablas
Fecha : 29/02/202x
Author : Jaime Gomez
'''

# Importando librerias
import mysql.connector
from mysql.connector import errorcode

#'''
# Crear tabla sin manejo de excepciones
config =  {"host":"localhost", 
           "user":"root", 
           "password":"", 
           "db":"hr6"}

conn = mysql.connector.connect(**config)

cur = conn.cursor()

sql = ( "CREATE TABLE employees ("
        "  emp_no int(11) NOT NULL AUTO_INCREMENT,"
        "  first_name varchar(14) NOT NULL,"
        "  last_name varchar(16) NOT NULL,"
        "  gender enum('H','M') NOT NULL,"
        "  hire_date date ,"
        "  birth_date date ,"
        "  PRIMARY KEY (emp_no)"
        ") ")

print(sql)
cur.execute(sql)
conn.close()

#'''

'''
# Crear tabla sin controlar excepciones

config =  {"host":"localhost", 
           "user":"prueba", 
           "password":"123456aB$", 
           "db":"hr"}

conn = mysql.connector.connect(**config)
cur = conn.cursor()

sql = ( "CREATE TABLE employees ("
        "  emp_no int(11) NOT NULL AUTO_INCREMENT,"
        "  first_name varchar(14) NOT NULL,"
        "  last_name varchar(16) NOT NULL,"
        "  gender enum('H','M') NOT NULL,"
        "  hire_date date ,"
        "  birth_date date ,"
        "  PRIMARY KEY (emp_no)"
        ") ")

print(sql)

try:
    cur.execute(sql)
except mysql.connector.Error as err:
    print(err.msg)
    if err.errno == \
                errorcode.ER_TABLE_EXISTS_ERROR:
        print("Tabla existe")
    else:
        print(err.msg)
else:
    print("OK")

conn.close()

#'''
