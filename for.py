#!/usr/bin/env python
#_*_ coding: utf8 _*_

# for = bucle


numero = int(raw_input("Numero: "))
mensaje = raw_input("Mensaje: ")

for m in range(0,numero):
	print("{} : {}".format(m,mensaje))