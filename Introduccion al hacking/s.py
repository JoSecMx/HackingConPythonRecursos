#!/usr/bin/env python
#_*_ coding: utf8 _*_

import sys
from shodan import Shodan

reload(sys)
sys.setdefaultencoding('utf8')
key = "shXLINeBiCP4FLh4IhvFiT2Ypbnh5PjK"

motor = Shodan(key)
try:
	query = motor.search("struts")
	print("Total de resultados: {}".format(query['total']))
	for host in query['matches']:
		print("IP: {}".format(host['ip_str']))
		print("Puerto: {}".format(host['port']))
		print("ORG: {}".format(host['org']))
		try:
			print("ASN: {}".format(host['asn']))
		except:
			pass
		for l in host['location']:
			print(l + " : " + str(host['location'][l]))

		print(host['data'])
except:
	print("Ocurrio un error")