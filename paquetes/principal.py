#!/usr/bin/env python
#_*_ coding: utf8 _*_

from paquete1 import calculadora_modulo

def main():
	while True:
		print("\nBienvenida\n")
		print("1.- Suma dos numeros")
		print("2.- Resta dos numeros")
		print("3.- Divide dos numeros")
		print("4.- Multiplica dos numeros")
		print("5.- Salir")
		opcion = int(raw_input("Opcion: "))

		if opcion == 1:
			valor1 = int(raw_input("Valor 1: "))
			valor2 = int(raw_input("Valor 2: "))
			calculadora_modulo.suma(valor1,valor2)

		elif opcion == 2:
			valor1 = int(raw_input("Valor 1: "))
			valor2 = int(raw_input("Valor 2: "))
			calculadora_modulo.resta(valor1,valor2)

		elif opcion == 3:
			valor1 = int(raw_input("Valor 1: "))
			valor2 = int(raw_input("Valor 2: "))
			calculadora_modulo.division(valor1,valor2)

		elif opcion == 4:
			valor1 = int(raw_input("Valor 1: "))
			valor2 = int(raw_input("Valor 2: "))
			calculadora_modulo.multiplicacion(valor1,valor2)
		elif opcion == 5:
			exit()

		else:
			print("\n Opcion invalida\n")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("\nSaliendo...")
		exit()
