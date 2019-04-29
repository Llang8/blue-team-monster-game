import random
class Board():

    def __init__(self,grid_size=4,fill_char="+"):
        # Initializes grid of grid_size * grid_size with the fill_char
        self.grid = [[fill_char]*grid_size]*grid_size
    
    # Prints the grid in its current state
    def printGrid(self):
        # Iterate through rows
        for x in range(len(self.grid)):
            # Iterate through columns in current row
            for y in range(len(self.grid[x])):
                # Print current character with space after
                print(self.grid[x][y], end=" ")

            # Move print to next line for next row
            print()

