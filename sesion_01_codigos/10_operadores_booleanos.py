
# Operadores booleanos


'''
  X         Y       AND
  False   False    False
  True    False    False
  False   True     False
  True    True     True

'''
a , b  = True, False
op1 = a and b  #  a & b 
print(op1)



'''
  X   Y   OR
  0   0    False
  0   1    True
  1   0    True
  1   1    True 
'''

op2 = a or b   #  a | b
print(op2)

op3  = not a
print(op3)


# Notaciones boleanas

#    A   B    AND   OR
#    F   F     F    F
#    F   T     F    T
#    T   F     F    T
#    T   T     T    T

estado1 = True
estado2 = False

print(estado1 and estado2)
print(estado1 & estado2)

print(estado1 or estado2)
print(estado1 | estado2)  # alt + 124

print( not estado1)
