from Tkinter import Tk, Button
from tkFont import Font

# class in which game takes places
class Board:

    # initializer
    def __init__(self):
        self.player = 'X' # by default, player is X
        self.computer = 'O' # computer opponent is O
        self.empty = '_' # empty spaces are denoted by underscores _
        self.size = 3 # default board size 3x3
        self.fields = {} # 2D array of board positions
        for y in range(self.size):
            for x in range(self.size):
                self.fields[x,y] = self.empty # initialize all positions to empty
            
    # executes a move in position (x,y) on the board        
    def move(self, x, y):
    
