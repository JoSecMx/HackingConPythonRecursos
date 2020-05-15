#!/usr/bin/env python
#_*_ coding: utf8 _*_


# pop nos sirve para eliminar el ultimo elemento de una lista
# del para borrar ciertos elementos de determinadas pocisiones
# ''.join(variable) nos ayuda a convertir una variable en una lista
# append nos ayuda a añadir nuevos elementos a una lista


lista = [1,2,3,4,5,6,7,8,"a","b","c",2.1,2.4,0.2,True,False]
lista1 = ['h','o','l','a']
lista1 = ''.join(lista1)
print(lista1)
print(lista[0:10])
lista.pop()
print(lista)
for l in lista:
	print(l)

del lista[1]
print(lista)

for n in range(90,100):
	lista.append(n)
print(lista)
lista.append("z")
print(lista)