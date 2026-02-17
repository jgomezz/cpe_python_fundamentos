'''
Curso : Programacion Basica de Python
Sesion : 04
Tema : Introduccion a Python -  Eliminar registros
Fecha : 29/02/202x
Author : Jaime Gomez
'''

# Importando librerias
import mysql.connector
from mysql.connector import errorcode

config =  {"host":"localhost", 
           "user":"root", 
           "password":"", 
           "db":"hr6"}
#'''
# Eliminar registros

conn = mysql.connector.connect(**config)
cur = conn.cursor()

sql = (" DELETE FROM employees "
        " WHERE emp_no =%s" ) 
values = (1,)

cur.execute(sql, values)
conn.commit()

print(cur.rowcount, "Fueron eliminados.")
conn.close()

#'''

'''
# Eliminar registros con manejo de errores

conn = mysql.connector.connect(**config)
cur = conn.cursor()

sql = (" DELETE FROM employees "
        " WHERE emp_no =%s" ) 
values = (1,)

try:
    cur.execute(sql, values)
    conn.commit()
    print(cur.rowcount, "Fueron eliminados.")
except mysql.connector.Error as err:
    print(err.msg)
else:
    print("OK")

conn.close()

#'''
