import sys

################################# HELPER CLASS #################################

#Randomize the first move to decide who plays#
class HelperFunctions(object):  

  # returns True if a spot is empty, otherwise False
  def is_taken(self, board, move):
    if board.positions[int(move)] != move:
      return True
    else: 
      return False  
      
  # checks to see if a character is a number between 1 and board.size*board.size
  # returns True if valid, False otherwise
  def is_valid_input(self, board, char):
    if isinstance(char, int):
      if char < 1:
        return False
      elif char > board.size*board.size:
        return False
      else:
        return True
    else:
      return False

  # takes in a board and a player and returns the winning configuration
  # if game has been won by that player, otherwise returns None
  def winning_configuration(self, board, player):
    # horizontal
    winningCombo = []
    j = 1
    while j <= board.size*board.size:
      winningCombo = []
      for i in range(j, j+3):
        if board.positions[i] == player:
          winningCombo.append(i)
      if len(winningCombo) == board.size:
        return winningCombo
      j = j+board.size
    # vertical
    if board.positions[1] == player and board.positions[1] == board.positions[4] and board.positions[4] == board.positions[7]:
      return [1, 4, 7]
    elif board.positions[2] == player and board.positions[2] == board.positions[5] and board.positions[5] == board.positions[8]:
      return [2, 5, 8]
    elif board.positions[3] == player and board.positions[3] == board.positions[6] and board.positions[6] == board.positions[9]:
      return [3, 6, 9]
    # diagonal
    if board.positions[1] == player and board.positions[1] == board.positions[5] and board.positions[5] == board.positions[9]:
      return [1, 5, 9]
    # other diagonal
    elif board.positions[3] == player and board.positions[3] == board.positions[5] and board.positions[5] == board.positions[7]:
      return [3, 5, 7]
    # if no wins
    else:
      return None

  def won_by(self, board, player):
    if self.winning_configuration(board, player) is None:
      return False
    else:
      return True

  # takes in a board and returns True if board has been completely filled 
  # and no one has won, False otherwise
  def is_tied(self, board):
    if self.won_by(board, board.player) or self.won_by(board, board.opponent):
      return False
    else:
      for key in board.positions.keys():
        if self.is_taken(board, str(key)) is False:
          return False
      return True
     
  # takes in a board and a player and returns all spaces occupied by that player
  def get_positions_of(self, board, player):
    spaces = []
    for i in range (1, 10):
      if board.positions[i] == player: 
        spaces.append(i)
    return spaces

  # returns "X" if player is "O" and vice versa
  def get_enemy_of(self, player):
    if player == board.player:
      return board.opponent
    else:
      return board.player

  # takes in a board and returns all currently empty spaces
  def get_open_positions(self, board):
    not_spaces = []
    for i in range(1, 10):
      if board.positions[i] != board.player and board.positions[i] != board.opponent:
        not_spaces.append(int(board.positions[i]))
    return not_spaces

  # returns True if the game has been completed (all spots filled)
  def is_complete(self, board):
    if len(self.get_open_positions(board)) == 0:
      return True
    else:
      return False

  # uses Minimax algorithm to return (score, space) representing 
  # the best possible next move given a board and a player.  
  def minimax(self, board, player):
    if self.is_complete(board): # if game is complete,
      if self.won_by(board, board.player):
        return (-1, None)
      elif self.won_by(board, self.get_enemy_of(board.player)):
        return (1, None)
      elif self.is_tied(board):
        return (0, None)
    elif player == board.player:
      best = (-2, None)
      for move in self.get_open_positions(board):
        board.positions[move] = player
        value = self.minimax(board, self.get_enemy_of(player))[0]
        board.positions[move] = str(move)
        if value > best[0]:
          best = (value, move)
      return best
    else:
      best = (2, None)
      for move in self.get_open_positions(board):
        board.positions[move] = player
        value = self.minimax(board, self.get_enemy_of(player))[0]
        board.positions[move] = str(move)
        if value < best[0]:
          best = (value, move)
      return best

################################# BOARD CLASS #################################
class Board (object):
  def __init__(self): 
    self.player = "X"
    self.opponent = "O"
    self.space = "*"
    self.size = 3
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
    print "\n" 
   
  # allows player to make a move
  def players_move(self):
    # if game has been won, end now
    if HelperFunctions.winning_configuration(HelperFunctions(), self, self.player) != None:
      print "Player has won the game with configuration ", HelperFunctions.winning_configuration(HelperFunctions(), self, self.player)
      sys.exit(0)
    if HelperFunctions.winning_configuration(HelperFunctions(), self, self.opponent) != None:
      print "Opponent has won the game with configuration ", HelperFunctions.winning_configuration(HelperFunctions(), self, self.opponent)
      sys.exit(0)
    if HelperFunctions.is_tied(HelperFunctions(), self):
      print "The game is tied!"
      sys.exit(0)

    print "The current open positions are: ", HelperFunctions.get_open_positions(HelperFunctions(), self)
    move = raw_input("\nMake your move, Player: ")
    
    #check that the input is a digit
    if move.isdigit() == False:
      print "You did not enter a valid number.  Please try again."
      self.players_move()
    # if input isn't on the board
    elif int(move) not in self.positions.keys():
      print "Your input does not exist on the board.  Please try again."
      self.players_move()
    # if spot is already taken
    elif HelperFunctions.is_taken(HelperFunctions(),self,move):
      print "This position is already taken. Choose a different move."
      self.players_move()
    elif HelperFunctions.is_valid_input(HelperFunctions(), board, int(move)) == False:
      print "This is not a valid move. Please choose again."
      self.players_move()
    else:
      print "\nYou entered", move
      self.positions[int(move)] = self.player
      self.to_string()
      print "Player now occupies spaces: ", HelperFunctions.get_positions_of(HelperFunctions(), self, self.player)
      print "Opponent now occupies spaces: ", HelperFunctions.get_positions_of(HelperFunctions(), self, self.opponent)
      print ""
      self.opponents_move()

  # uses Minimax algorithm to make an opponents' move
  def opponents_move(self):
    # if game has been won, end now
    if HelperFunctions.winning_configuration(HelperFunctions(), self, self.player) != None:
      print "Player has won the game with configuration ", HelperFunctions.winning_configuration(HelperFunctions(), self, self.player)
      sys.exit(0)
    elif HelperFunctions.winning_configuration(HelperFunctions(), self, self.opponent) != None:
      print "Opponent has won the game with configuration ", HelperFunctions.winning_configuration(HelperFunctions(), self, self.opponent)
      sys.exit(0)
    elif HelperFunctions.is_tied(HelperFunctions(), self):
      print "The game is tied!"
      sys.exit(0)
    else:
      optimalmove = HelperFunctions.minimax(HelperFunctions(), self, self.opponent)[1]
      print "Opponent chooses: ", optimalmove
      self.positions[optimalmove] = self.opponent
      self.to_string()
      print "Player now occupies spaces: ", HelperFunctions.get_positions_of(HelperFunctions(), self, self.player)
      print "Opponent now occupies spaces: ", HelperFunctions.get_positions_of(HelperFunctions(), self, self.opponent)
      print ""
      self.players_move()
    
################################# SCRIPT #################################    

board = Board()
board.to_string()
board.players_move()