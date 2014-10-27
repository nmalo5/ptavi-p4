#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.
# Dirección IP del servidor.
try:
    SERVER = sys.argv[1]
    PORT = int(sys.argv[2])
    # Contenido que vamos a enviar
    METHOD = sys.argv[3]
    LINE = sys.argv[4]
    EXPIRES = int(sys.argv[5])
except IndexError:
    sys.exit("Usage: client.py ip puerto register sip_address expires_value")
except ValueError:
    sys.exit("Usage: client.py ip puerto register sip_address expires_value")

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))

print "Enviando: " + METHOD.upper() + " sip:" + LINE + " SIP/2.0\r\n\r\n"
print "Enviando: " + str(EXPIRES)
LINE_EXPIRES = "Expires: " + str(EXPIRES) + '\r\n\r\n'
my_socket.send(METHOD.upper() + " sip:" + LINE + " SIP/2.0\r\n" + LINE_EXPIRES)
data = my_socket.recv(1024)

print 'Recibido -- ', data
print "Terminando socket..."

# Cerramos todo
my_socket.close()
print "Fin."
