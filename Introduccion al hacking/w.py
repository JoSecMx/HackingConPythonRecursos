#!/usr/bin/env python
#_*_ coding: utf8 _*_


import shutil
import sys
import os

def main():
	print(len(sys.argv))
	if len(sys.argv) == 2:
		for n in range(0,int(sys.argv[1])):
			shutil.copy(sys.argv[0],sys.argv[0]+str(n))
	else:
		print("Faltan argumentos")

if __name__ == '__main__':
	main()