#!/usr/bin/env python
# coding: utf8

import socket

HOST = ''       # Client IP address
PORT = 5001     # Client port

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)


class Client:

    @staticmethod
    def setup(self):
        """
        Set up the host
        """
        with open('config.txt') as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        print(content)

        if len(content) != 4:
            print('Arquivo de configuração possui uma quantidade inválida de linhas!')

        self.ip_address = content[0].split(':', 1)[0]
        self.port = int(content[0].split(':', 1)[1])
        self.nickname = content[1]
        self.token_time = int(content[2])

        if content[3].lower() == 'true':
            self.token = True
        else:
            self.token = False

        print(self.ip_address)
        print(self.port)
        print(self.nickname)
        print(self.token_time)
        print(self.token)


client = Client()
client.setup(client)

while True:
    msg, client_udp = udp.recvfrom(1024)
    print(client_udp, msg)
    destination = (client.ip_address, client.port)
    udp.sendto(msg, destination)
    print('sent!')
