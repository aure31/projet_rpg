import socket
from _thread import *
from packet import *


class Player:

    player_list = {}
    max_ID = 0
    render_distance = 5

    def __init__(self,username:str,coord:tuple[int],conn:socket.socket):
        self.ID = Player.max_ID
        Player.max_ID += 1
        self.username = username
        self.conn = conn
        self.x = coord[0]
        self.y = coord[1]
        Player.player_list[self.ID] = self

    def send_packet(self,packet:packet):
        self.conn.send(str.encode(packet))

    def spawn_packet(self):
        return self.username + "," + str(self.x) + "," + str(self.y) 
    
    def get_player(ID:int):
        return Player.player_list[ID]
        

    