'''
Curso : Programacion Basica de Python
Sesion : 04
Tema : Introduccion a Python -  Insertar registros
Fecha : 29/02/202x
Author : Jaime Gomez
'''

# Importando librerias
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime, date

config =  {"host":"localhost", 
           "user":"root", 
           "password":"", 
           "db":"hr6"}

''' 
# Insertar un registro
conn = mysql.connector.connect(**config)
cur = conn.cursor()

sql = ("INSERT INTO employees "
        "(first_name, last_name, hire_date, "
        " gender, birth_date) "
        "VALUES (%s, %s, %s, %s, %s)")


values = ('Juan', 'Valdez', None, 'H', None) 

cur.execute(sql,values)

emp_no = cur.lastrowid
print("Nro. de empleado " , emp_no)

conn.commit()

conn.close()

#'''

#''' 
# Insertar un registro con error

conn = mysql.connector.connect(**config)
cur = conn.cursor()

sql = ("INSERT INTO employees "
        "(first_name, last_name, hire_date, gender, birth_date) "
        "VALUES (%s, %s, %s, %s, %s)")

values = ('Jaime', 'Gomez', None, 'H', None) 

try:
    cur.execute(sql,values)
    emp_no = cur.lastrowid
    print("Nro. de empleado " , emp_no)
    conn.commit()
except mysql.connector.Error as err:
    print(err.msg)
else:
    print("OK")

conn.close()

#'''



#''' Insertar de un registro

conn = mysql.connector.connect(**config)
cur = conn.cursor()

tomorrow = datetime.now().date()

sql = ("INSERT INTO employees "
        "(first_name, last_name, hire_date, gender, birth_date) "
        "VALUES (%s, %s, %s, %s, %s)")
values = ('Juan', 'Valdez', tomorrow, 'H', date(1980, 6, 14)) 

cur.execute(sql,values)

emp_no = cur.lastrowid
print("Numero de empleado " , emp_no)

conn.commit()

conn.close()

#'''


''' Insertar de un registro con error

conn = mysql.connector.connect(**config)
cur = conn.cursor()

tomorrow = datetime.now().date()

sql = ("INSERT INTO employees "
        "(first_name, last_name, hire_date, gender, birth_date) "
        "VALUES (%s, %s, %s, %s, %s)")
values = ('Juan', 'Valdez', tomorrow, 'H', date(1980, 6, 14)) 

cur.execute(sql,values)

emp_no = cur.lastrowid
print("Numero de empleado " , emp_no)

conn.commit()

conn.close()

#'''


#'''

# Insercion de varios registro

conn = mysql.connector.connect(**config)
cur = conn.cursor()

tomorrow = datetime(2020,3,1)
#tomorrow = datetime.now().date()

sql = ("INSERT INTO employees "
        "(first_name, last_name, hire_date, gender, birth_date) "
        "VALUES (%s, %s, %s, %s, %s)")
values = (
    ('Juan', 'Valdez', tomorrow, 'M', date(1980, 6, 14)),
    ('Maria', 'Rosado', tomorrow, 'M', date(1990, 10, 24)),
    ('Percy', 'Maldonado', tomorrow, 'M', date(2000, 6, 23)))

cur.executemany(sql,values)

conn.commit()
print(cur.rowcount, "fueron insertados.")
conn.close()

#'''
