## Introducción a Clases en Python

<img src="uml.png"/>


```python

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
```


## Ejemplo de una tabla
|Titulo|Descripcion|Observacion|
|-|-|-|
|Python|Lenguaje de Programacion|-|
|Java|Lenguaje de Programacion|-|
