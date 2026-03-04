"""
Diccionarios en Python - Parte 2

"""
bancos = {
    "BCP" : "Banco de Credito del Peru",
    "BBVA" : "Banco Bilbao Vizcaya Argentaria",
    "SCO" : "Scotiabank Peru",
    "IBK" : "Banco Interamericano de Finanzas"
}

'''
- Imprimir el nombre de cada banco en mayuscula
- Adaptar el diccionario para que se incluya el nro. de importancia de cada banco
  // BCP, BBVA, SCO, IBK

'''
bancos = {
    "BCP" : {
        "nombre" : "Banco de Credito del Peru",
        "posicion" : 1
    },
    "BBVA" : "Banco Bilbao Vizcaya Argentaria",
    "SCO" : "Scotiabank Peru",
    "IBK" : "Banco Interamericano de Finanzas"
}


print(f"El banco {bancos['BCP']['nombre']} es el banco con la posición {bancos['BCP']['posicion']} del Perú")