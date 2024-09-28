
from enum import Enum

class packet_type(Enum):
    PING = 0
    DISCONNECT = 1
    MOVE = 4

    def get(val:int):
        return packet_type._value2member_map_[val]