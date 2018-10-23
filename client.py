import socket

HOST = ''       # Client IP address
PORT = 5001     # Client port

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)

'''
    Set up the host
    :argument Path to config file
    :returns None
'''


def set_up():
    data = open('config.txt', 'r')
    print data.read()


set_up()
while True:
    msg, client = udp.recvfrom(1024)
    print client, msg
    destination = (HOST, PORT)
    udp.sendto(msg, destination)
