#!/usr/bin/env python
#_*_ coding: utf8 _*_


class Carro(object):
	def __init__(self,m):
		self.color = "Rojo"
		self.puertas = 4
		self.tipo = "Deportivo"
		self.m = m
	def movilidad(self):
		if self.m == True:
			print("Acelerar")
		else:
			print("Frenar")

def main():
	while True:
		print("1 Acelerar")
		print("2 Frenar")
		valor = int(raw_input("> "))
		if valor == 1:
			c = Carro(True)
			c.movilidad()
		else:
			c = Carro(False)
			c.movilidad()
	#print(c.color)
	#print(c.puertas)
	#print(c.tipo)

if __name__ == '__main__':
	main()