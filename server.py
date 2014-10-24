
#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco
en UDP simple
"""

import SocketServer
import sys

class EchoHandler(SocketServer.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        print self.client_address
        while 1:
            line = self.rfile.read()
            if not line:
                break
        self.wfile.write("Hemos recibido tu peticion")
        print "El cliente nos manda " + line

if __name__ == "__main__":
    LISTEN_PORT = int(sys.argv[1])
    # Creamos servidor de eco y escuchamos
    serv = SocketServer.UDPServer(("", LISTEN_PORT ), EchoHandler)
    print "Lanzando servidor UDP de eco..."
    serv.serve_forever()
