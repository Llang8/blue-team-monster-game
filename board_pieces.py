import random
import math
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
        
    def printEggs(self):
        print("Eggs collected: {}".format(self.eggs))

    # Returns true if player is in same tile as passed item
    def checkCollision(self,item):
        return item.x == self.x and item.y == self.y

class Monster(Character):
    def __init__(self,x,y,char="@"):
        super().__init__(x,y)
        self.char = char

    # Move monster randomly but keep on screen
    def move(self, board):
        board.grid[self.y][self.x] = board.fill_char
        direction = math.floor(random.random() * 4)
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