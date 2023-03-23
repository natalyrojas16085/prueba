primera_lista = ['manzana', 'banano']
print(primera_lista)
lista1 = [2, 4, 5, 83, 3.14]
print(lista1)
lista2 = ["a", 123, "b", 3.1416, 'palabra', True, 1000]
print(lista2)
# tamaño de una lista  (len)
print(len(lista1))
print(len(lista2))
# tipo de dato lista
print('tipo de dato lista')
print(type(lista1))
print(type(12))
# otraa lista
num = [1, 2, 3, 4, 5]
print(num)
num2 = list([1, 2, 3, 5, 6])
print(num2)
print("index list:")
print(num[0])
print(num[0:3])
print(num[-1::-1])
print(3 in num)
print(10 in num)
#listas 2 cambiar datos ( es mutable)
num=[9,34,25,56,72]
print(num)
num[1]=88
print(num)
#num=[9,88,25,56,72]
# funcion insert
num.insert(1,77)
print(num)
# funcion append #num=[9,77,88,25,56,72]
num.append(100)
print(num)
num2=[9,8,7]
print(num)
# funcion extend:
num.extend(num2)
print(num)
# funcion remove #num=[9,88,25,56,72,100,9,8,7]
num.remove(100)
print(num)
num.pop(2)
print(num)