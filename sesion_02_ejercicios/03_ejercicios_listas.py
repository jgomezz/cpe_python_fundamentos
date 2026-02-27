
'''
Ejercicio : En la lista dada, 

nros = [101,210,335,450,510,601,702]

a) Mostrar todos los elementos de la lista a excepción del 210 y 510
b) Mostrar los elementos de la lista que son mayores a 300
c) Mostrar el promedio de los elementos de la lista
'''

# Uso de append
participantes = ["Vanessa", "Jose", "Cesar"]
print(participantes)

participantes.append("Joaquin")
print(participantes)

participantes.append("Ursula")
print(participantes)

participantes.append("Jose")
participantes.append("Irma")
print(participantes)

participantes.extend(["Ricardo", "Milagros"])
print(participantes)

#del(participantes[0])
#print(participantes)

# Atenciones

participante_atender = participantes.pop(0)
print(participante_atender)
print(participantes)

participante_atender = participantes.pop(0)
print(participante_atender)
print(participantes)

'''
100, 101, .........., 199

Generar una lista con los números del 100 al 199,
luego retirar los primeros 15 ticket y mostrarlos en una lista aparte.
'''


'''
Fragmento del Quijote

En efecto, rematado ya su juicio, vino a dar en el más extraño pensamiento que jamás dio loco en el mundo, y fue que le pareció convenible y necesario, así para el aumento de su honra como para el servicio de su república, hacerse caballero andante

'''

fragmento = "En efecto, rematado ya su juicio, vino a dar en el más extraño pensamiento que jamás dio loco en el mundo, y fue que le pareció convenible y necesario, así para el aumento de su honra como para el servicio de su república, hacerse caballero andante"


print(fragmento)

