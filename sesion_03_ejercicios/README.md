## Introducción a Clases en Python

<img src="imagenes/uml.png"/>


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



### Ejercicio Propuesto de clases

- Crear la clase InstitutoEducativo que tengas los atributos
codigo, nombre, ubicacion, descripcion, anho_fundacion, ruc
- Debe tener los metodos : obtener_ruc , obtener_info
- Usarlo para crear 3 objetos de institutos



## Introducción a Herencias en Python

<img src="imagenes/herencias.png"/>


```python


# Clase Base
class Empleado:

    def __init__(self, nombre, apellido, ciudad):
        self.nombre = nombre
        self.apellido = apellido
        self.ciudad = ciudad

    def obtener_nombre_completo(self):
        return self.nombre + " " + self.apellido
    

# Clase hijas

class Administrador(Empleado):
    pass

class Desarrollador(Empleado):
    pass

class Instructor(Empleado):
    pass


admin = Administrador("Juan","Sanchez","Lima")

des = Desarrollador("Jaime","Gomez","Trujillo")

instructor = Instructor("Maria","Perez","Arequipa")


print(admin.obtener_nombre_completo())
print(des.obtener_nombre_completo())
print(instructor.obtener_nombre_completo())
```

## Herencias y sobrecargas en Python

<img src="imagenes/herencias_completa.png"/>


```python

print('----------- Segunda Version ------------------')


# Clase Base
class Empleado:

    def __init__(self, nombre, apellido, ciudad):
        self.nombre = nombre
        self.apellido = apellido
        self.ciudad = ciudad

    def obtener_nombre_completo(self):
        return self.nombre + " " + self.apellido
    

# Clase hijas

class Administrador(Empleado):
    
    def __init__(self, nombre, apellido, ciudad, especialidad):
        super().__init__(nombre, apellido, ciudad) # Llamada al constructor de la clase base    
        self.especialidad = especialidad

    def obtener_residencia(self):
        return f"El administrador {self.nombre} vive en {self.ciudad} "

    def obtener_nombre_completo(self):
        return "Es una informacion confidencial"


class Desarrollador(Empleado):
    
    def __init__(self, nombre, apellido, ciudad, experto_lenguaje_prog):
        super().__init__(nombre, apellido, ciudad) # Llamada al constructor de la clase base    
        self.experto_lenguaje_prog = experto_lenguaje_prog

    def obtener_experiencia(self):
        return f"El desarrollador {self.nombre} es experto en {self.experto_lenguaje_prog}"



class Instructor(Empleado):
    
    def __init__(self, nombre, apellido, ciudad, anhos_exp, nombre_curso):
        super().__init__(nombre, apellido, ciudad) # Llamada al constructor de la clase base    
        self.anhos_exp = anhos_exp
        self.nombre_curso = nombre_curso

    def obtener_exp_instructor(self):
        return f"El instructor {self.nombre} tiene {self.anhos_exp} años de experiencia y dicta el curso de {self.nombre_curso}"

print('----------- Administrador ------------------')

admin = Administrador("Juan","Sanchez","Lima","Redes")
print(admin.obtener_residencia())
print(admin.obtener_nombre_completo())

print('----------- Desarrollador ------------------')

des = Desarrollador("Jaime","Gomez","Trujillo","Python")
print(des.obtener_experiencia())

print('----------- Instructor ------------------')

instructor = Instructor("Maria","Perez","Arequipa",5,"IA")
print(instructor.obtener_exp_instructor())
```

### Ejercicio Propuesto de Herencias de clases


<img src="imagenes/herencias_ejercicio.png"/>




## Ejemplo de una tabla
|Titulo|Descripcion|Observacion|
|-|-|-|
|Python|Lenguaje de Programacion|-|
|Java|Lenguaje de Programacion|-|
