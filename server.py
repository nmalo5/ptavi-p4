
#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco
en UDP simple
"""

import SocketServer
import sys

class SIPRegisterHandler(SocketServer.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        print self.client_address
        while 1:
            line = self.rfile.read()
            line_partida = line.split(":")
            Method = line_partida[0].split(" ")[0]
            if Method == "REGISTER": 
                Clave = line_partida[1].split(" ")[0]
                Registro[Clave] = self.client_address[0]
            if not line:
                break
        self.wfile.write("SIP/2.0 200 OK\r\n\r\n")
        print "REGISTRO " + str(Registro)

if __name__ == "__main__":
    LISTEN_PORT = int(sys.argv[1])
    Registro = {}
    # Creamos servidor de eco y escuchamos
    serv = SocketServer.UDPServer(("", LISTEN_PORT ), SIPRegisterHandler)
    print "Lanzando servidor UDP de eco..."
    serv.serve_forever()
