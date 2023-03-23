#Condicional if
adivinar = 50
number = int(input('Sr usuario, digite un número: '))
#if('prueba lógica o condición')
'''if (number > 50):
  print('verdadero')
  print(number * 2)
else:
  print('falso')

print('la instrución "if" termino')'''

if (number > adivinar):
  print('Disminuye el valor del número')
elif (number < adivinar):
  print('Aumenta el valor del número')
else:
  print('Adivinaste el número')

print('la instrución "if" termino')
# if anidado 2
'''if (number >= adivinar):
  print('coloque un numero menor')
else:
  print('Acertado')
else:
  print('coloque un numero mayor')
'''
