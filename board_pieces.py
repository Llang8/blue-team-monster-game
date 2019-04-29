class Character():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def moveCharacter(self,dir):
        pass

class Player(Character):
    eggs = 0
    def __init__(self,x,y,char="P"):
        super().__init__(x,y)
        self.char = char

    # If on monster tile kill player
    # If on egg tile add one to egg count
    # If on door check if all eggs are collected and change level if needed
    def checkCollision(self):
        pass

class Monster(Character):
    def __init__(self,x,y,char="@"):
        super().__init__(x,y)
        self.char = char

class Egg():
    def __init__(self,x,y,char="0"):
        self.x = x
        self.y = y
        self.char = char

class Door():
    def __init__(self,x,y,char="|"):
        self.x = x
        self.y = y
        self.char = char