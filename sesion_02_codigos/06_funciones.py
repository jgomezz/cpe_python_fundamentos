'''
Curso : Programacion Basica de Python
Sesion : 02 
Tema : Introduccion a Python -  Funciones
Fecha : 15/02/2020
Author : Jaime Gomez

'''

'''
nros = [20,21,22,23,24,25,26]
size = len(nros)   # funcion nativa de Python
print(size)
#'''

###################################
#    Creacion de funcion
###################################


def sumar(ope1, ope2, op3=0):
    #ope1 = 4
    #ope2 = 8
    suma = ope1+ope2 + op3
    #print(suma)
    return suma

sumar(4, 8, 3)
sumar(14, 18)
res = sumar(4, 18)
print(res)
print("--------- ")










'''
 
   Input ---> f(x)  ---> Output
  
'''
def my_print(msg, nro_v = 4):
    for i in range(nro_v):
        print(msg)

message = "Hola Mundo ...!"
nro_times = 10 
my_print(message,nro_times)
my_print(message)    # llamada a funcion sin parametros

'''
Crear una funcion, que tengas 2 argumentos
a y b , debera imprimir los numero comprendidos
entre a y b . No considerar los valor a y b
'''

'''
 
   Input ---> f(x)  
  
'''

# Solucion 1
def Imprimir(a,b):
    for i in range(a+1,b):
        print(i)

Imprimir(2,8)

# Solucion 2
def funcion(a,b):
    if(a>b):
        for c in range(b+1,a):          
            print(c)
    elif a==b:
        print('¡no hay numeros para mostrar!')
    else :
        for c in range(a+1,b):
            print(c)

a=2   # int(input('ingrese el primer numero: '))
b=8   # int(input('ingrese el segundo numero: '))
funcion(a,b)



# La declaración de la función
def mi_funcion(limite = 2):
    '''
     Funcion  que imprime los primeros 
     numeros hasta el valor de limite-1
    '''
    for n in range(limite):
        print("valor",n)

# invoca a la función
mi_funcion(5)
mi_funcion()
#help(mi_funcion)

''' 
 crear una funcion que me imprima la longitud de 
 un arreglo
'''

def calc_longitud_2(A):
    cont = 0
    for n in A:
        cont +=1
    print(cont)   

def calc_longitud(dato):
    s = len(dato)
    return s 


nros = [20,21,22,23,24,25,26]
l = calc_longitud(nros)

print("la longitud es =",l)

'''
    I --> f(x) --> O

'''
def suma(a,b):
    s = a + b   
    #print(s)
    return s

a = 4 
b = 5
#c = a + b
c = suma(a,b)
print(c)

'''
  listado = ["Tecsup","Lima","Python"]
  obtener_tamanho(var) : obtiene el tamanho de la lista
  tamanho
'''

# Solucion 1
def obtener_tamanho(lista):
    tamanho=len(lista)
    return tamanho

listado = ["Tecsup","Lima","Python"]
tamanio=obtener_tamanho(listado)
print(tamanio)


# Solucion 2
listado= ["tecsup","lima","python"]
def taman(dato):
    s=len(dato)
    return s

c=taman(listado)
print(c)


# Solucion 3
listado = ["Tecsup","Lima","Python"]

def obtener_tamanho(var_x):
    return len(var_x)

print (obtener_tamanho(listado))








'''

      INPUT -->  FUNCTION  --> OUTPUT

'''

'''
 Crear la función inc que tiene 2 argumentos :
    a , i 

    def inc(a, i):

    En a va el valor hacer incrementado
    En i es el valor a incrementar
    Se debe devolver el valor incrementado

    Ejemplo:
    
    s = inc(4,2)  # s debe valer 6    

'''

def inc(a, i):
    ret = a + i 
    return ret

s = inc(5,2)
print("El valo incrementado es=",s)

'''
     
           *
   1 2 3 4 5 6 7 8 9
       -       -

'''

def extremos(a, i):
    es = a + i  
    ei = a - i 
    return ei, es

inf, sup =  extremos(5,2)
print("El valor inferior =",inf)
print("El valor superior =",sup)

'''
Crear la funcion ope_mat (a, b)
sum, res, mul, div = ope_mat(a,b)
'''

# Solucion 1
def ope_mat(a,b):
    return a+b, a-b, a*b,a/b

sum,res,mul,div =  ope_mat(10,8)
print ("la suma es:",sum)
print ("la resta es:",res)
print ("la multiplicacion  es:",mul)
print ("la division es:",div)

# Solucion 2
a=5
b=9
def ope_mat(a,b):
    suma=a+b
    resta=a-b
    multi=a*b
    divi=a/b
    return suma,resta,multi,divi

sumi, res, mul, div = ope_mat(a,b)

print("las respuestas son: ",sumi," ",res," ",mul," ",div)

# Solucion 3
def extremos(a, b):
    sum = a + b  
    res = a - b
    mul = a * b
    div = a / b
    return sum, res, mul, div
sum,res,mul,div =  extremos(5,2)
print("sum =",sum)
print("res =",res)
print("mul =",mul)
print("div =",div)


'''
 Ejercicio : ejecutar en un funcion
 las 4 operaciones matematicas 
 basicas, ingresando como texto
 el nombre de la operacion.
'''
def ope_mat(nombre_ope, a,b):
    r = None
    if nombre_ope == "suma" :
        r = a + b
    elif nombre_ope == "resta" :
        r = a - b
    return r

res  =  ope_mat("resta",10,8)
print(res)

# Solucion
def ope_mat(nombre_ope, a,b):
    r = None
    if nombre_ope == "suma" :            r = a + b
    elif nombre_ope == "resta" :         r = a - b
    elif nombre_ope == "multiplicacion": r = a * b
    elif nombre_ope == "division":       r = a / b
    return r

res  =  ope_mat("division",10,8)
print(res)


# Pasar como parametro el nombre
# de una funcion




'''
 Ejercicio : Ejecutar las
 4 operaciones matematicas
 pasando como parametro
 el nombre de la funcion
 a llamar
'''

def suma(a,b): return a+b
                
def ope_mat_v2(func, a, b):
    return func(a,b)

res  =  ope_mat_v2(suma,20,18)
print(res)


'''
' FRONT '   <--->  ' BACK' 
'''

# MVC : Model - View  - Controller

# M : Modelo
def pow(a,b) : return a**b
def suma(a,b): return a+b
def resta (a,b): return a-b
def multiplicacion (a,b): return a*b
def division (a,b): return a/b

#
def es_valido(func): return True

# C : Controlador
def ctrl_procesos(func, a, b):

    r = -1 
    if es_valido(func) :
        r = func(a,b)

    return r

# V : Como se ingresan los datos 100 y 200

res  =  ctrl_procesos(division,100,200)
print(res)

'''

Elabore una función que tome como argumento 
tres números enteros y devuelva el mayor

'''

def nombre_que_desees(a,b,c):
    '''
    '''
    return 



def mayor(a,b,c):
    if a>b and a>c:
         return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
num_mayor=mayor(27,35,78)
print(num_mayor)


def mayor(a,b,c):
    aux1=[a,b,c]
    aux2=0
    for i in range(len(aux1)):
        if aux1[i]>aux2:
            aux2=aux1[i]
    return aux2
c=mayor(15,5,3)
print(c)



def mayor2(a,b,c):
    aux1=[a,b,c]
    return max(aux1)


def mayor2(a,b,c,d):
    aux1=[a,b,c,d]
    return max(aux1)
    

def mayor2(a,b,c,d,e):
    aux1=[a,b,c,d,e]
    return max(aux1)

'''
Funcion para calcular el mayor
valor de varios argumentos sin
un limite definido
'''
def mayor_v2(*args):

    aux1 = []
    for arg in args:
        aux1.append(arg)

    return max(aux1)

c = mayor_v2(15,5,3,4,11)
print(c)



def extremos_2(a, i):
    es = a + i  #  inc(a, i)
    ei = a - i 
    return (ei, es)

limites = extremos_2(5,2)
print("El valor inferior =",limites[0])
print("El valor superior =",limites[1])


#a, b, c, d = hacer_algo(777)


#######################################
#              Scope
#######################################


# Caso 1
def hacer_algo():
    numero = 8
    print("Numero desde funcion() :",numero)

numero = 10
hacer_algo()
print("Numero desde invocacion :",numero)

# Caso 2
def hacer_algo_2():
    print("Numero desde funcion() :",numero)

numero = 10
hacer_algo_2()
print("Numero desde invocacion :",numero)


'''
# Caso 3
def hacer_algo_3():
    pass
    numero += 8 # no se puede modificar, error sintaxis

numero = 10
hacer_algo_3()
print("Numero desde invocacion :",numero)
'''

#######################################
#       Funcion como parametro
#######################################

def exec_ope(nombre_func, a, b) :
    '''
    Funcion que invoca a otra 
    funcion en tiempo de ejecucion
    '''
    ret = nombre_func(a,b)

    return ret

def suma(a,b): 
    return a+b

res =  exec_ope(suma, 4, 5)

print(res)


def resta(a,b): 
    return a-b


res =  exec_ope(resta, 4, 5)
print(res)

#######################################
#       Funcion como retorno
#######################################

def imprimir_nro(n):
    for i in range(n):
        print(i+1)

def retorna_funcion():
    print("Retorna otra funcion")
    return imprimir_nro

retorna_funcion()(13)   
