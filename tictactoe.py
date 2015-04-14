import sys

#Randomize the first move to decide who plays#

class Board (object):
   def __init__(self): 
    self.player = "X"
    self.opponent = "O"
    self.space = "*"
    self.positions = {
        1: "1", 
        2: "2",
        3: "3",
        4: "4", 
        5: "5", 
        6: "6", 
        7: "7", 
        8: "8", 
        9: "9"}
       
        
   def to_string(self):
     print " "
     print "Your Current Board is:"
     for i in range(1, 4):
      sys.stdout.write( "%s " % self.positions[i])
     print " "
     for i in range(4, 7):
      sys.stdout.write( "%s " % self.positions[i])
     print " "
     for i in range(7, 10):
      sys.stdout.write( "%s " % self.positions[i])
     print " " 
   
   def players_move(self):
    move = raw_input("Make your move: ")
    print "You entered", move
    self.positions[int(move)] = self.player
    self.to_string()
    
  
    
    
board = Board()
board.to_string()
board.players_move()


   
    

