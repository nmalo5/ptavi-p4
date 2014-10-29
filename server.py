#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor register SIP
"""

import SocketServer
import sys

PORT = int(sys.argv[1])


class SIPRegisterHandler(SocketServer.DatagramRequestHandler):
    """
    SIP server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write("Hemos recibido tu peticion")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            print "El cliente nos manda " + line
            print "IP Cliente: " + self.client_address[0]
            print "IP Puerto: " + str(self.client_address[1]) + "\n"
            if not line:
                break

if __name__ == "__main__":
    # Creamos servidor SIP y escuchamos
    serv = SocketServer.UDPServer(("", PORT), SIPRegisterHandler)
    print "Lanzando servidor SIP..."
    serv.serve_forever()
