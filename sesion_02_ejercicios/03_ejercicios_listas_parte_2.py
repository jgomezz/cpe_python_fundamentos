'''
Fragmento del Quijote

En efecto, rematado ya su juicio, vino a dar en el más extraño pensamiento que jamás dio loco en el mundo, y fue que le pareció convenible y necesario, así para el aumento de su honra como para el servicio de su república, hacerse caballero andante

'''

# Base de NLP : Tokenización, Stemming, Lematización, Stop Words

fragmento = "En efecto, rematado ya su juicio, vino a dar en el más extraño pensamiento que jamás dio loco en el mundo, y fue que le pareció convenible y necesario, así para el aumento de su honra como para el servicio de su república, hacerse caballero andante"

print("------------------------------------")
print(fragmento)
print("------------------------------------")

palabras = fragmento.split(" ")
print(palabras)
print("------------------------------------")

fragmento_unido = " ".join(palabras)
print(fragmento_unido)      
print("------------------------------------")

fragmento_unido = "_".join(palabras)
print(fragmento_unido)      
print("------------------------------------")
