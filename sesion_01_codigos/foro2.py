'''
Ejercicio 1 : Imprimir la siguiente serie usando while
81, 78, 75 , 72, 69 , 66 , 63, 60

'''
cont = 81

while cont >= 60:
    print(cont)
    cont -= 3

'''
Sumar los 20 primeros números pares, pero no
considerar los mùltiplos de 4  
'''
suma = 0
num = 0     # numero a sumar                        

while num < 2*20:

    num += 2
    
    if num % 4 != 0:
        suma += num

print("suma =", suma)