
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


print('----------- Tercera Version ------------------')

class Docente:

    # Constructor de la clase
    def __init__(self, codigo, nombre, apellido, edad):
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


    def obtener_info(self):
        ret = f'Código: {self.codigo}, Nombre: {self.nombre} {self.apellido}, Edad: {self.edad}'
        return ret
    
    def obtener_login(self):
        ret = self.nombre[0].lower() + self.apellido.lower()
        return ret


doc_jaime = Docente(1, 'Jaime', 'García', 30) # Se instancia una clase
doc_gerardo = Docente(2, 'Gerardo', 'Martínez', 25) # Se instancia una clase
doc_enrique = Docente(3, 'Enrique', 'López', 35) # Se instancia una clase

print(doc_jaime.obtener_info())
print(doc_jaime.obtener_login())

print('----------- Cuarta Version ------------------')

class Docente:

    institucion = "UTEC" # Atributo de clase

    # Constructor de la clase
    def __init__(self, codigo, nombre, apellido, edad):
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


    def obtener_info(self):
        ret = f'Código: {self.codigo}, Nombre: {self.nombre} {self.apellido}, Edad: {self.edad}'
        return ret
    
    def obtener_login(self):
        ret = self.nombre[0].lower() + self.apellido.lower()
        return ret

doc_jaime = Docente(1, 'Jaime', 'García', 30) # Se instancia una clase
doc_gerardo = Docente(2, 'Gerardo', 'Martínez', 25) # Se instancia una clase
doc_enrique = Docente(3, 'Enrique', 'López', 35) # Se instancia una clase


print(doc_jaime.obtener_info())
print(doc_gerardo.obtener_info())

print(doc_jaime.institucion)
print(doc_gerardo.institucion)
print(doc_enrique.institucion)

print('>> Modifico el atributo de clase a través de la instancia doc_jaime')
doc_jaime.institucion = "TECSUP"

print(doc_jaime.institucion)
print(doc_gerardo.institucion)
print(doc_enrique.institucion)

print('>> Modifico el atributo de clase a través de la clase Docente')
Docente.institucion = "TECSUP"

print(doc_jaime.institucion)
print(doc_gerardo.institucion)
print(doc_enrique.institucion)