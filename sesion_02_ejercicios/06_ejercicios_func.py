
def f_suma(x,y):

    s = x + y
  
    return s




a = 11
b = 2132
suma  = a + b
print(suma)

suma  = f_suma(a,b)
print(suma)

a = 4
b = 6
#suma  = a + b
suma  = f_suma(a,b)
print(suma)



a = 2
b = 80
#suma  = a + b
suma  = f_suma(a,b)
print(suma)


'''
Crear la funcion f_operacion que reciba 3 parametros, a, b y ope,
dependiendo del valor de ope, se realizara la suma, resta, multiplicacion o division de a y b

   f_operacion(3,5,'suma')
   f_operacion(3,5,'resta')
   f_operacion(3,5,'mult')
   f_operacion(3,5,'div')


'''

print("-----------------Ejercicio propuesto---------------------------")

def f_suma(x,y=10):
    s = x + y  
    return s

a = 2
b = 80
suma  = f_suma(a,b)
print(suma)

suma  = f_suma(a)
print(suma)