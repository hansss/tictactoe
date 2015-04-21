import sys

################################# HELPER CLASS #################################

#Randomize the first move to decide who plays#
class HelperFunctions(object):  

  # returns True if a spot is already taken, otherwise False
  def is_taken(self, board, move):
    if board.positions[int(move)] != move:
      return True
    else: 
      return False  
    

  # takes in a board and a player returns the winning configuration, 
  # if game has been won by the player, otherwise returns None

  ## def is_won_by(board, player):

  # takes in a board and returns True if board has been completely filled 
  # and no one has won, False otherwise

  def is_tied(self, board):
    for key in board.positions.keys:
      if self.is_taken(self, board, board.positions[key]) and (self.is_won_by(board, board.player) or self.is_won_by(board, board.opponent)):
        True
      else:
        False

     
  # takes in a board and a player and returns all spaces occupied by that player
  ## def get_positions_of(board, player):

  # returns X if player is O and vice versa
  def get_enemy_of(player):
    if player == board.player:
      return board.opponent
    else: return board.player

  # takes in a board and returns all currently empty spaces
  ## def get_open_positions(board):

################################# BOARD CLASS #################################
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
       
  # returns string representation of Board     
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
   
  # allows player to make a move
  def players_move(self):
    move = raw_input("Make your move: ")
    
    #check that the spot is not taken
    if move.isdigit() and int(move) in self.positions.keys():
      if HelperFunctions.is_taken(HelperFunctions(),self,move):
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
    
    #check that the input is 1-9
    #check if this is a winning move

    

  # uses Minimax algorithm to make an opponents' move
  ## def opponents_move(self):
    
################################# SCRIPT #################################    

board = Board()
board.to_string()
board.players_move()