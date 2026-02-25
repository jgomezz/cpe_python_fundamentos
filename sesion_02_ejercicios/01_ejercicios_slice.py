'''
Dado la cadena
numeros="0123456789"

- Obtener los numeros pares en una cadena, omitir el 0
- Obtener los numeros impares en una cadena

'''
numeros="0123456789"

nro_pares = numeros[2:10:2]
print(nro_pares)

nro_pares = numeros[2::2]
print(nro_pares)


numeros="0123456789"

nro_impares = numeros[1:10:2]
print(nro_impares)

nro_impares = numeros[1::2]
print(nro_impares)


# Invertir una cadena

#odalnuM aloH

cadena = "odnuM aloH"
cadena_invertida = cadena[-1:-11:-1]
print(cadena_invertida)
cadena_invertida = cadena[::-1]
print(cadena_invertida)
