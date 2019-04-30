import random

class Board():
    grid = [[]]
    def __init__(self,grid_size=4,fill_char="+",eggs=1):
        # Initializes grid of grid_size * grid_size with the fill_char
        self.grid_size = grid_size
        self.fill_char = fill_char
        self.eggs = eggs
        for row in range(grid_size):
            for col in range(grid_size):
                self.grid[row].append(fill_char)
            self.grid.append([])
    
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
    def addItems(self,items):
        for item in items:
            self.grid[item.y][item.x] = item.char
