# import Affichage as scr
class Player():
    def __init__(self,username,coo=["scr.s.CENTER.x,scr.s.CENTER.y"],hp=50,money=0,inventory={'sword':None,'shield':None}):
        """
        Constructeur de la classe Player.
        Initialise un joueur avec un nom d'utilisateur, des coordonnées, des points de vie, de l'argent et un inventaire.
        """
        self.username = username
        self.coo = coo
        self.hp = hp
        self.money = money
        self.inventory = inventory

    def __repr__(self):
        """
        Représentation sous forme de chaîne de caractères du joueur.
        Affiche les détails du joueur : nom d'utilisateur, coordonnées, points de vie, argent et inventaire.
        """
        return f"===== username : {self.username} ======\ncoo : {self.coo}\nhp : {self.hp} {(self.hp//10)*'♡'}\nmoney : {self.money}\ninventory : {self.inventory}\n====="

    def is_dead(self):
        """
        Vérifie si le joueur est mort.
        Retourne True si les points de vie (hp) sont inférieurs ou égaux à 0, sinon False.
        """
        if self.hp > 0:
            return False
        return True
    
    def take_damage(self,amount):
        """
        Applique des dégâts au joueur.
        Si le montant de dégâts est supérieur à 50, le joueur est mis à 0 hp. 
        Sinon, les points de vie du joueur sont réduits du montant de dégâts.
        """
        if amount > 50:
            self.hp = 0
        else :
            self.hp -= amount

    def heal(self,amount):
        if amount > 0:
            self.take_damage(-amount)
    
    def give_money(self,amount):
        """
        Ajoute de l'argent au joueur.
        Le montant d'argent spécifié est ajouté à la balance actuelle du joueur.
        """
        self.money += amount

    def give_item(self,item): # give an item or upgrade it
        """
        Ajoute un objet à l'inventaire ou améliore l'objet existant.
        Si l'objet n'est pas encore dans l'inventaire, il est initialisé à 0. 
        Sinon, le niveau de cet objet dans l'inventaire est augmentée de 1.
        """
        if self.inventory[item] == None:
            self.inventory[item] = 0
        else :
            self.inventory[item]+=1

class Enemy():
    def __init__(self,index="goblin",hp=5,ad=2,asp=0.3,range=1,special=None):
        self.index = index
        self.hp = hp
        self.ad = ad
        self.asp = asp
        self.range = range

Enemy_list = {"goblin":Enemy(),"gargouille":Enemy("gargouille",15,6,0.8,5,None)}

class NPC():
    def __init__(self,name):
        self.name = name

def get_enemy_list():
    ch = ""
    for elem in Enemy_list:
        ch+=f"===== index : {elem} =====\nhp : {Enemy_list[elem].hp}\nattack damage : {Enemy_list[elem].ad}\n"
    print(f'Voici la liste des ennemis présents et utilisables dans le jeu ainsi que leur caractéristiques :\n{ch}=====')

def jeu_de_test_joueur():
    joueur = Player('Adrien')
    # print(joueur)
    joueur.take_damage(18)
    joueur.give_money(-30)
    joueur.give_money(15)
    for _ in range(21):
        joueur.give_item('sword')
    print(joueur)
    print(joueur.is_dead())

get_enemy_list()