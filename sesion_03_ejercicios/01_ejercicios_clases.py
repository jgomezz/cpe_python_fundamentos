
print('----------- Primera Version ------------------')


'''
 Clase docente
'''
class Docente:
    pass


doc_jaime = Docente() # Se instancia una clase

doc_gerardo = Docente() # Se instancia una clase

doc_enrique = Docente() # Se instancia una clase

print(doc_jaime)
print(doc_gerardo)
print(doc_enrique)


print('----------- Segunda Version ------------------')

class Docente:

    # Constructor de la clase
    def __init__(self, codigo, nombre, apellido, edad):
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


doc_jaime = Docente(1, 'Jaime', 'García', 30) # Se instancia una clase
doc_gerardo = Docente(2, 'Gerardo', 'Martínez', 25) # Se instancia una clase
doc_enrique = Docente(3, 'Enrique', 'López', 35) # Se instancia una clase

print(doc_jaime.nombre)
print(doc_gerardo.nombre)
print(doc_enrique.nombre)
