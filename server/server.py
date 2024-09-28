import socket
import _socket
from _thread import *
import time
from packet import *
from player import *

server = "127.0.0.1"
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen()
print("Waiting for a connection, Server Started")

def threaded_client(conn:_socket.socket):
    conn.send(str.encode(str(packet(send_packet_type.PING, ""))))
    data = conn.recv(2048)

    player = Player()
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending : ", reply)

            conn.sendall(str.encode(reply))
        except:
            break
    print("Lost connection")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, conn)