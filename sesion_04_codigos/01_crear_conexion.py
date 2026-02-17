'''
Curso : Programacion Basica de Python
Sesion : 04
Tema : Introduccion a Python -  Conexion a BBDD
Fecha : 08/03/2022
Author : Jaime Gomez
Version : 1.2
'''


'''
Comando para instalar el driver de la base de datos en Python


python -m pip install mysql-connector-python
python -m pip uinstall mysql-connector-python

C:/Users/jgomez/AppData/Local/Programs/Python/Python310/python -m pip install mysql-connector-python

Crear usuario:

    CREATE USER 'prueba'@'localhost' 
    IDENTIFIED  BY '123456aB$';

    GRANT ALL PRIVILEGES ON *.* TO 'prueba'@'localhost';

Cadena de conexion:

    config =  {"host":"localhost", 
            "user":"prueba", 
            "password":"123456aB$",  
            "db":"world"}

'''

# Importando librerias
import mysql.connector

'''
config =  {"host":"localhost", 
           "user":"root", 
           "password":"",  
           "db":"mysql"}

conn = mysql.connector.connect(**config)

print(conn)

conn.close()

#'''

# Importando librerias
import mysql.connector
from mysql.connector import errorcode

#'''
config =  {"host":"localhost", 
           "user":"root", 
           "password":"",  
           "db":"mysql2"}

conn = None

try:

    conn = mysql.connector.connect(**config)

except mysql.connector.Error as err:

    if err.errno ==  errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error con el usuario o la clave")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Base de datos no existe")
    else:
        print(err)
else:
    conn.close()

print(conn)

#if conn != None: conn.close()

#'''


"""

https://dev.mysql.com/doc/world-setup/en/

https://dev.mysql.com/doc/world-setup/en/world-setup-installation.html

mysql> SOURCE /Users/mactecsup/Downloads/world.sql;

mysql> USE world

"""


'''
Comando para instalar el driver de la 
base de datos en Python

python -m pip install mysql-connector
python -m pip uinstall mysql-connector

Crear usuario:

    CREATE USER 'prueba'@'localhost' 
    IDENTIFIED WITH mysql_native_password BY '123456aB$';

    GRANT ALL PRIVILEGES ON *.* TO 'prueba'@'localhost';

Cadena de conexion:

    config =  {"host":"localhost", 
            "user":"prueba", 
            "password":"123456aB$",  
            "db":"world",
            "auth_plugin":"mysql_native_password"}

'''