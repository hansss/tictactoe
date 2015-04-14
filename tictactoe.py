#Randomize the first move to decide who plays#

class Board (object):
   def __init__(self): 
    self.player = "X"
    self.opponent = "O"
    self.space = "*"
    self.positions = []
    for i in range (1, 9):
     self.positions.append(str(i))
     
   def to_string(self):
    for i in range(1, 3): 
        print self.positions[i] + " "
    print "\n"
    for i in range(4, 6):
        print self.positions[i] + " " 
    print "\n"
    for i in range(7, 9):
        print self.positions[i] + " " 
    print "\n"
    
board = Board()
board.to_string()
    

