from socket import *
from _thread import *
from enum import Enum
from server_entity import *


class send_packet_type(Enum):
    PING = 0
    DISCONNECT = 1
    NEW_ENTITY = 2
    SPAWN = 3
    MOVE = 4
    MAP = 5
    UPDATE_POS = 6

    def get(val:int):
        return send_packet_type._value2member_map_[val]
    
class receive_packet_type(Enum):
    PONG = 0
    DISCONNECT = 1
    MOVE = 2

    def get(val:int):
        return receive_packet_type._value2member_map_[val]


class send_packet:
    def __init__(self,packet_type:send_packet_type,data:str):
        self.packet_type = packet_type
        self.data = data
    
    def __str__(self) -> str:
        return str(self.packet_type + "/" + self.data)
    
    def bytes_to_packet(data:bytes):
        decode = data.decode("utf-8")
        split = decode.split("/")
        return send_packet(send_packet_type.get(split[0]),split[1])
    
class ping_packet(send_packet):
    def __init__(self):
        super().__init__(send_packet_type.PING,"")

class disconnect_packet(send_packet):
    def __init__(self):
        super().__init__(send_packet_type.DISCONNECT,"")

class new_entity_packet(send_packet):
    def __init__(self,entity:Server_entity):
        super().__init__(send_packet_type.NEW_ENTITY,str(entity))

class spawn_packet(send_packet):
    from player import Player
    def __init__(self,player:Player):
        super().__init__(send_packet_type.SPAWN,player.packet())

class update_map(send_packet):
    from player import Player
    def __init__(self,map:int[Player.render_distance][Player.render_distance]):
        super().__init__(send_packet_type.MAP,str(map))

class update_pos(send_packet):
    from player import Player
    def __init__(self,player:Player):
        super().__init__(send_packet_type.UPDATE_POS,player.packet())


    