#!/usr/bin/env python
#_*_ coding: utf8 _*_

archivo = open('archivo1.txt','a')

dedicacion = raw_input("Dedicacion: ")
empresa = raw_input("Empresa: ")
idioma = raw_input("Idioma: ")

archivo.write("\n")
archivo.write(dedicacion)
archivo.write("\n")
archivo.write(empresa)
archivo.write("\n")
archivo.write(idioma)

archivo.close()
