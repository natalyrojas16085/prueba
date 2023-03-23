number = int(input('digite un numero : '))

#operaciones relacionales o de comparacion
print(number > 3)
print(number >= 3)
print(number < 3)
print(number <= 3)
print(number == 3)

#operaciones logicas

print("operaciones logicas.")
print('conjunción & and')
print(True and True)
print((number <= 3) and True)
print(True and False)
print((number <= 3) and False)

print('disyunción | or')
print(False or True)
print(True or False)
print(False or False)
print(number > 3 or number < 10)
print(number <= 3 or number >= 10)

print('Negación NOT,~')
print(not (False))

print('or exclusiva ^')
print(True ^ True)
print(False ^ False)
print(True ^ False)
#**OPERACIONES DE PERTENENCIA**
#in: se usa para preguntar si una letra esta en una variable
print('operador in')
nombre = 'Nataly Rojas'
print('J' in nombre)
print('N' in nombre)
