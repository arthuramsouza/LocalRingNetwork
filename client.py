#!/usr/bin/env python
# coding: utf8

import socket

HOST = ''   # Client IP address
PORT = 271  # Client port

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)


class Client:

    ip_address = ''
    port = 0
    nickname = ''
    token_time = 0
    token = False

    @staticmethod
    def setup():
        """
        Set up the host
        """
        with open('config.txt') as f:
            content = f.readlines()
        content = [x.strip() for x in content]

        if len(content) != 4:
            print('Arquivo de configuração possui uma quantidade inválida de linhas!')

        Client.ip_address = content[0].split(':', 1)[0]
        Client.port = int(content[0].split(':', 1)[1])
        Client.nickname = content[1]
        Client.token_time = int(content[2])

        if content[3].lower() == 'true':
            Client.token = True
        else:
            Client.token = False

    @staticmethod
    def get_config():
        print(Client.ip_address)
        print(Client.port)
        print(Client.nickname)
        print(Client.token_time)
        print(Client.token)

    @staticmethod
    def receive():

        while True:
            msg, client_udp = udp.recvfrom(1024)
            print(client_udp, msg)

            header = str(msg).replace("b'", "").replace("'", "").strip().lower()
            print(header)

            if header == 'ok':
                print('OK')
            elif header == 'error':
                print('error')
            else:
                print('não copiado')

    @staticmethod
    def send():
        msg = 'nãocopiado' + input()

        while msg != '\x18':
            print(Client.ip_address)
            print(Client.port)
            udp.sendto(bytes(msg, encoding='utf8'), (Client.ip_address, Client.port))
            msg = 'nãocopiado' + input()
