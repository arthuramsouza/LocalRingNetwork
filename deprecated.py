#!/usr/bin/env python
# coding: utf8

import socket

HOST = '127.0.0.1'      # Client IP address
PORT = 5001             # Client port

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destination = (HOST, PORT)

print('Use CTRL + X to exit')

msg = input()

while msg != '\x18':
    udp.sendto(bytes(msg, encoding='utf8'), destination)
    msg = input()

udp.close()
