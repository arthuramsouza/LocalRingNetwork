from client import Client
from threading import Thread

# Set up the client
Client.setup()

# Create two threads
try:
    thread_receive = Thread(target=Client.receive, args=())
    thread_send = Thread(target=Client.send, args=())
    thread_receive.start()
    thread_send.start()
except:
    print("Error: unable to start thread")

while 1:
    pass
