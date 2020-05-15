#!/usr/bin/env python
#_*_ coding: utf8 _*_

# w = write

archivo = open("archivo1.txt","w")
nombre = raw_input("Nombre: ")
edad = raw_input("edad: ")
pais = raw_input("pais: ")

archivo.write(nombre)
archivo.write("\n")
archivo.write(edad)
archivo.write("\n")
archivo.write(pais)

print("E escrito los datos")

archivo.close()