import random

class Board():

    def __init__(self,grid_size=4,fill_char="+"):
        # Initializes grid of grid_size * grid_size with the fill_char
        self.grid = [[fill_char]*grid_size]*grid_size
    
    # Prints the grid in its current state
    def printGrid(self):
        # Iterate through rows
        for row in range(len(self.grid)):
            # Iterate through columns in current row
            for column in range(len(self.grid[row])):
                # Print current character with space after
                print(self.grid[row][column], end=" ")

            # Move print to next line for next row
            print()

    # Pass in a list of objects to spawn
    def addItems(self,list):
        for item in list:
            print(item.x,item.y,item.char)
            self.grid[item.y][item.x] = item.char

