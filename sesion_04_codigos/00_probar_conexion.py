
# Importando librerias
import mysql.connector
from mysql.connector import errorcode

#'''
config =  {"host":"localhost", 
           "user":"root", 
           "password":"",  
           "db":"hr"}

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