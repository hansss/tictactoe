import sys

#Randomize the first move to decide who plays#
class HelperFunctions(object):  
   def not_taken(self, board, move):
     if board.positions[int(move)] != move:
      return True
     else: 
      return False  
      
   #def valid_character
     

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
    
    #check that the spot is not taken
    if move.isdigit() and int(move) in self.positions.keys():
     if HelperFunctions.not_taken(HelperFunctions(),self,move):
      print "This position is already taken. Choose a different move."
      self.players_move()
     else:
      print "You entered", move
      self.positions[int(move)] = self.player
      self.to_string()
      self.players_move()
    else:
      print "This is not a valid move. Please choose again."
      self.players_move()
    
     
    """
    if HelperFunctions.not_taken(HelperFunctions(),self,move):
     print "This position is already taken. Choose a different move."
     self.players_move()
    else:
     return self.keys()
    
     if move in self.keys():
      print "You entered", move
      self.positions[int(move)] = self.player
      self.to_string()
      self.players_move()
     else:
      print "This is not a valid move. Please choose again."
      self.players_move()
  """
    
    #check that the input is 1-9
    #check if this is a winning move

    

board = Board()
board.to_string()
board.players_move()


   
    

