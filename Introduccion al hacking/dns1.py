#!/usr/bin/env python
#_*_ coding: utf8 _*_

import dns.resolver

def main():
	try:
		a = dns.resolver.query("google.com","ANY")
		for q in a:
			print(q)
	except:
		print("No pude obtener la consulta")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()