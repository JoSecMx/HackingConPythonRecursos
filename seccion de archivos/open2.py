#!/usr/bin/env python
#_*_ coding: utf8 _*_


archivo = open('wordlist.lst','r')

lista = archivo.read().split('\n')
for n in lista:
	print(n)