from grid import Board
from board_pieces import *
import keyboard

# Handles button presses
# Called when a button is pressed from the keyboard.on_press hook
# Calls Player.move() and passes the direction to move
def check_input(event):
    if event.name == 'up':
        print('UP')
    elif event.name == 'left':
        print('LEFT')
    elif event.name == 'right':
        print('RIGHT')
    elif event.name == 'down':
        print('DOWN')

# Main code loop
def main():
    board = Board(10,"+")
    player = Player(5,5)
    egg = Egg(8,6)
    monster = Monster(4,3)
    board.addItems([player,egg,monster])
    board.printGrid()
    while True:
        pass

# This sets up a hook that listens for 
keyboard.on_press(check_input)

main()