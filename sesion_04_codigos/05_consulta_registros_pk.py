'''
Curso : Programacion Basica de Python
Sesion : 04
Tema : Introduccion a Python -  Consulta de registros
Fecha : 29/02/202x
Author : Jaime Gomez
'''

# Importando librerias
import mysql.connector
from mysql.connector import errorcode
import datetime

config =  {"host":"localhost", 
           "user":"root", 
           "password":"", 
           "db":"hr6"}

'''
# Consulta de registros
conn = mysql.connector.connect(**config)
cur = conn.cursor()
sql = (" SELECT first_name, last_name "
       " FROM employees "
       " WHERE last_name = %s")

values = ("Valdez",)

cur.execute(sql, values)

for first_name, last_name in cur: 
    print("{}, {}".format(last_name, first_name))

conn.close()

#'''

'''
# Consulta de registros
conn = mysql.connector.connect(**config)
cur = conn.cursor()

sql = (" SELECT first_name, last_name "
       " FROM employees "
       " WHERE last_name = %s")

values = ("Valdez",)

try:
    cur.execute(sql, values)
    for first_name, last_name in cur: 
        print("{}, {}".format(last_name, first_name))
except mysql.connector.Error as err:
    print(err.msg)
else:
    print("OK")

conn.close()

#'''


'''
# Consulta de registros
conn = mysql.connector.connect(**config)
cur = conn.cursor()
sql = (" SELECT first_name, last_name, hire_date "
       " FROM employees "
       " WHERE hire_date BETWEEN %s AND %s")

hire_start = datetime.date(2020, 1, 1)
hire_end = datetime.date(2020, 4, 1)

values = (hire_start, hire_end)
cur.execute(sql, values)

#for reg in cur: 
#    print(reg)

for first_name, last_name, hire_date in cur: 
    #print(first_name," -- " , last_name, "---",hire_date)
    print("{}, {} fue contratado el {:%d %b %Y}"
    .format(last_name, first_name, hire_date))

conn.close()

#'''

'''
# Consulta de registros con manejo de errores
conn = mysql.connector.connect(**config)
cur = conn.cursor()
sql = (" SELECT first_name, last_name, hire_date "
       " FROM employees "
       " WHERE hire_date BETWEEN %s AND %s")

hire_start = datetime.date(2020, 1, 1)
hire_end = datetime.date(2020, 4, 1)

values = (hire_start, hire_end)
cur.execute(sql, values)

#for reg in cur: 
#    print(reg)

for first_name, last_name, hire_date in cur: 
    #print(first_name," -- " , last_name, "---",hire_date)
    print("{}, {} fue contratado el {:%d %b %Y}"
    .format(last_name, first_name, hire_date))

conn.close()

#'''

