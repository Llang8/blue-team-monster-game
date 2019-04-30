from grid import Board
from board_pieces import *
import keyboard
import random
import math

# import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 
  
# Player object
player = None
# Board Object
board = None

# Handles button presses
# Called when a button is pressed from the keyboard.on_press hook
# Calls Player.move() and passes the direction to move
def check_input(event):
    # Pull in global variables
    global board
    global player

    # Move character based on button pressed
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

# Clear function used to clear the terminal/console output 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

# Returns a random number between 0 and the board size
def randomPosition():
    global board
    return math.floor(random.random() * board.grid_size)

# Main code loop
def main():

    # Pull in global variables
    global board
    global player

    # Initialize board of size 4x4, fill with '+'
    board = Board(4,"+")
    # Initialize Player object at position x=0 y=board size / 2
    player = Player(0,math.floor(board.grid_size/2))
    # Initialize Door in last column middle row
    door = Door(board.grid_size - 1, math.floor(board.grid_size/2))
    # Initialize Egg object at random position
    x = randomPosition()
    y = randomPosition()
    # Make sure position is not the same as the player or door
    while (x == player.x and y == player.y) or (x == door.x and y == door.y):
        x = randomPosition()
        y = randomPosition() 
    egg = Egg(x,y)
    # Initialize Monster at random position not equal to door, player, or egg positions
    while (x == player.x and y == player.y) or (x == egg.x and y == egg.y) or (x == door.x and y == door.y):
        x = randomPosition()
        y = randomPosition()
    monster = Monster(x,y)

    # Add items to board
    # TODO: Make this work in case of multiple eggs
    board.addItems([player,egg,monster,door])
    board.printGrid()

    # Current level logic
    while True:
        # Clear console
        clear()
        # Print grid and egg count
        board.printGrid()
        player.printEggs()
        # Check collisions with egg, if true increment eggs and remove egg from screen
        if player.checkCollision(egg):
            player.eggs+=1
            # Once egg has been collected move off screen
            egg.x = -1
            egg.y = -1
        # Check collisions with monster, if true player loses
        if player.checkCollision(monster):
            print("You lose!")
            break
        # Check collisions with door
        if player.checkCollision(door):
            # If player has collected all of the eggs move to next level
            if player.eggs == board.eggs:
                print("You passed the level! Moving to the next...")
                sleep(2)
                break
        # Make code wait here to prevent refreshing too fast
        monster.move(board)
        # Readd items to board (Don't add egg if already collected, will throw error)
        if egg.x >= 0 and egg.y >= 0:
            board.addItems([player,egg,monster,door])
        else:
            board.addItems([player,monster,door])
        sleep(.3)
# This sets up a hook that listens for 
keyboard.on_press(check_input)

main()