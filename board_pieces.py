class Character():
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Player(Character):
    eggs = 0
    def __init__(self,x,y,char="P"):
        super().__init__(x,y)
        self.char = char

    def moveCharacter(self,direction,board):
        print(direction)
        board.grid[self.y][self.x] = board.fill_char
        if direction == 0:
            if self.y > 0:
                self.y-=1
        elif direction == 3:
            if self.x > 0:
                self.x-=1
        elif direction == 2:
            if self.y < board.grid_size - 1:
                self.y+=1
        elif direction == 1:
            if self.x < board.grid_size - 1:
                self.x+=1
        board.grid[self.y][self.x] = self.char
        

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