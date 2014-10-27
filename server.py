#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco
en UDP simple
"""

import SocketServer
import sys
import time


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
            """Si tenemos Register, procedemos a rellenar nuestro Registro"""
            if Method == "REGISTER":
                """Primero comprobamos los tiempos de expiracion"""
                for Client in Registro.keys():
                    #Vamos comparando con el tiempo de cada clave-valor
                    Tiempo = Registro[Client][1]
                    if time.time() >= Tiempo:
                        del Registro[Client]
                        print "REGISTRO " + str(Registro)
                Clave = line_partida[1].split(" ")[0]
                Expires = line_partida[2].split(" ")[1]
                Time = time.time() + int(Expires)
                Valores = [self.client_address[0], Time]
                Registro[Clave] = Valores
                print "REGISTRO " + str(Registro)
                """ Si entramos con un valor a 0, somos borrados"""
                if int(Expires) == 0:
                    del Registro[Clave]
                    print "REGISTRO " + str(Registro)
                self.register2file()
                self.wfile.write("SIP/2.0 200 OK\r\n\r\n")
            if not line:
                break

    def register2file(self):
        """ Método que escribirá en nuestro fichero"""
        fichero = open('registered.txt', 'w')
        fichero.write("User\tIP\tExpires\n")
        for Client in Registro:
            IP = Registro[Client][0]
            Tiempo = time.gmtime(Registro[Client][1])
            Time = time.strftime('%Y-%m-%d %H:%M:%S', Tiempo)
            fichero.write(Client + '\t' + IP + '\t' + Time + '\n')
        fichero.close()

if __name__ == "__main__":
    LISTEN_PORT = int(sys.argv[1])
    Registro = {}
    # Creamos servidor de eco y escuchamos
    serv = SocketServer.UDPServer(("", LISTEN_PORT), SIPRegisterHandler)
    print "Lanzando servidor UDP de eco..."
    serv.serve_forever()
