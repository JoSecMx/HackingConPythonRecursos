#!/usr/bin/env python
#_*_ coding: utf8 _*_

import sys
from shodan import Shodan

reload(sys)
sys.setdefaultencoding('utf8')


def main():
	api = Shodan('shXLINeBiCP4FLh4IhvFiT2Ypbnh5PjK')
	h = api.host('123.57.0.34')
	print('''

		Direccion: {}
		Ciudad: {}
		ISP: {}
		Org: {}
		Puertos: {}

		'''.format(h['ip_str'],h['city'],h['isp'],h['org'],h['ports']))

	file = open('escaneo.txt','a+')

	for elemento in h['data']:
		lista = elemento.keys()
		for l in lista:
			file.write(str(elemento[l]))

	file.close()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()