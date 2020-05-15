#!/usr/bin/env python
#_*_ coding: utf8 _*_

from Wappalyzer import WebPage, Wappalyzer

def main():
	wap = Wappalyzer.latest()
	try:
		web = WebPage.new_from_url("https://curso--python-0-pruebas.000webhostapp.com/")
		tecnologias = wap.analyze(web)
		for t in tecnologias:
			print("Tecnologia detectada: {}".format(t))
	except:
		print("Ha ocurrido un error")
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Saliendo")
		exit()