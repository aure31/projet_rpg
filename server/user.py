from _socket import _Address

class user:

    def __init__(self,adress:_Address,username:str) -> None:
        self.adress = adress
        self.username = username

    