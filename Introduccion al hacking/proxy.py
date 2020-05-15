#!/usr/bin/env python
#_*_ coding: utf8 _*_


import requests

def main():
	proxy = {'http':'http://119.28.88.98:1080'}
	a1 = requests.get('http://httpbin.org/ip')
	a2 = requests.get('http://httpbin.org/ip',proxies=proxy)

	print('''

	 	IP Real: {}  IP con Proxy: {}

	 	'''.format(a1.text,a2.text))

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()