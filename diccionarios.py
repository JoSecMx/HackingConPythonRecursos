#!/usr/bin/env python
#_*_ coding: utf8 _*_

diccionario = dict(nombre="alumno",plataforma="Udemy",edad=18)
# items 
#print(diccionario)
#a = diccionario.items()
#print(a)

#copy
#b = diccionario.copy()
#print(b)


# keys

# keys = diccionario.keys()
#print(keys)

# values

#values = diccionario.values()
#print(values)

for n in diccionario.keys():
	print("{} Su valor es: {}".format(n,diccionario[n]))