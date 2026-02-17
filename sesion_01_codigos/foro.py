'''
Se define las categorias salariales

Categoria 1 y 2 ganan 10000 soles

Categoria 3 y 4 ganan 7000 soles

Categoria 5 ganan 5000 soles

para las otras categorias ganan 3000 soles

Se pide un programa donde se ingrese la categoria
y obtenga el salario

''' 

salario = 0
cat = input("Ingrese la categoria: ")


if cat == '1' or cat == '2':
    salario = 10000
elif cat == '3' or cat == '4':
    salario = 7000
elif cat == '5':
    salario = 5000
else :  
    salario = 3000

print(f"El salario es {salario}")