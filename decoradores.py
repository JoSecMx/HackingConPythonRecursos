#!/usr/bin/env python
#_*_ coding: utf8 _*_

# classmethod
# staticmethod
# property


class prueba1(object):
	def __init__(self,radio):
		self.radio = radio

	@classmethod # Nos ayuda a usar una funcion sin que antes la clase sea atribuida a un objeto
	def saludo(cls,nombre):
		print("Hola {}".format(nombre))

	@staticmethod #Nos yuda a trabajar con funciones sin argumentos
	def saludo_static():
		print("Bienvenido")

	@property #Con property trabajamos con funciones como si fueran variables al usar 'return'
	def area_circulo(self):
		return 3.1416*(self.radio**2)
def main():
	#nombre = raw_input("Nombre: ")
	#prueba1.saludo(nombre)
	c = prueba1(5)
	area = c.area_circulo
	print(area)

if __name__ == '__main__':
	main()