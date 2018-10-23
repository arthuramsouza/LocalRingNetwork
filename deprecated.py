import socket

HOST = '127.0.0.1'      # Client IP address
PORT = 5001             # Client port

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destination = (HOST, PORT)

print 'Use CTRL+X to exit\n'

msg = raw_input()

while msg != '\x18':
    udp.sendto(msg, destination)
    msg = raw_input()

udp.close()
