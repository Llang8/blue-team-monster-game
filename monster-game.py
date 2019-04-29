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
    board = Board(10,"+")
    player = Player(randomPosition(),randomPosition())
    egg = Egg(randomPosition(),randomPosition())
    monster = Monster(randomPosition(),randomPosition())
    board.addItems([player,egg,monster])
    board.printGrid()
    randomPosition()
    while True:
        clear()
        board.printGrid()
        sleep(.25)

# This sets up a hook that listens for 
keyboard.on_press(check_input)

main()