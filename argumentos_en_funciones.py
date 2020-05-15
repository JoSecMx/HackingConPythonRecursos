#!/usr/bin/env python
#_*_ coding: utf8 _*_

def saludo(nombre1,edad1):
	print("Hola {} tienes: {}".format(nombre1,edad1))


def main():
	nombre = raw_input("Nombre: ")
	edad = int(raw_input("Edad: "))
	saludo(nombre,edad)

if __name__ == '__main__':
	main()