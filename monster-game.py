from grid import Board
from board_pieces import *
import keyboard
import random
import math

# import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 
  

player = None
board = None
# Handles button presses
# Called when a button is pressed from the keyboard.on_press hook
# Calls Player.move() and passes the direction to move
def check_input(event):
    global board
    global player
    if event.name == 'up':
        try:
            player.moveCharacter(0,board)
        except:
            pass
    elif event.name == 'right':
        try: 
            player.moveCharacter(1,board)
        except:
            pass
    elif event.name == 'down':
        try:
            player.moveCharacter(2,board)
        except:
            pass
    elif event.name == 'left':
        try:
            player.moveCharacter(3,board)
        except:
            pass

# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

def randomPosition():
    global board
    return math.floor(random.random() * board.grid_size)

# Main code loop
def main():
    global board
    global player
    board = Board(4,"+")
    player = Player(0,math.floor(board.grid_size/2))
    egg = Egg(randomPosition(),randomPosition())
    monster = Monster(randomPosition(),randomPosition())
    door = Door(randomPosition(),randomPosition())
    board.addItems([player,egg,monster,door])
    board.printGrid()
    randomPosition()
    for i in range(1,4):
        while True:
            clear()
            board.printGrid()
            player.printEggs()
            if player.checkCollision(egg):
                player.eggs+=1
                # Once egg has been collected move off screen
                egg.x = -1
                egg.y = -1
            if player.checkCollision(monster):
                print("You lose!")
                break
            if player.checkCollision(door):
                if player.eggs == board.eggs:
                    print("You passed the level! Moving to the next...")
                    sleep(2)
                    break
            sleep(.3) 

# This sets up a hook that listens for 
keyboard.on_press(check_input)

main()