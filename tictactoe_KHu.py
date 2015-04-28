import sys

################################# HELPER CLASS #################################

#Randomize the first move to decide who plays#
class HelperFunctions(object):  

  # allows player to make a move (go in helper)
  def players_move(self, board):
    # if game has been won, end now
    if board.winning_configuration(board.player) != None:
      print "Player has won the game with configuration ", board.winning_configuration(board.player)
      sys.exit(0)
    if board.winning_configuration(board.opponent) != None:
      print "Opponent has won the game with configuration ", board.winning_configuration(board.opponent)
      sys.exit(0)
    if board.is_tied():
      print "The game is tied!"
      sys.exit(0)

    print "The current open positions are: ", board.get_open_positions()
    move = raw_input("\nMake your move, Player: ")
    
    #check that the input is a digit (go in helper)
    if move.isdigit() == False:
      print "You did not enter a valid number.  Please try again."
      self.players_move()
    # if input isn't on the board
    elif int(move) not in board.positions.keys():
      print "Your input does not exist on the board.  Please try again."
      self.players_move()
    # if spot is already taken
    elif board.is_taken(move):
      print "This position is already taken. Choose a different move."
      self.players_move()
    elif board.is_valid_input(int(move)) == False:
      print "This is not a valid move. Please choose again."
      self.players_move()
    else:
      print "\nYou entered", move
      board.make_move(int(move), board.player)
      board.to_string()
      print "Player now occupies spaces: ", board.get_positions_of(board.player)
      print "Opponent now occupies spaces: ", board.get_positions_of(board.opponent)
      print ""
      self.opponents_move(board)

  # uses Minimax algorithm to make an opponents' move (go in helper)
  def opponents_move(self, board):
    # if game has been won, end now
    if board.winning_configuration(board.player) != None:
      print "Player has won the game with configuration ", board.winning_configuration(board.player)
      sys.exit(0)
    elif board.winning_configuration(board.opponent) != None:
      print "Opponent has won the game with configuration ", board.winning_configuration(board.opponent)
      sys.exit(0)
    elif board.is_tied():
      print "The game is tied!"
      sys.exit(0)
    else:
      if board.is_about_to_win() != None:
        print "Opponent chooses: ", board.is_about_to_win()
        board.make_move(int(board.is_about_to_win()), board.opponent)
      else:
        optimalmove = self.minimax(board, board.opponent, 1)[1]
        print "Opponent chooses: ", optimalmove
        board.make_move(int(optimalmove), board.opponent)
      board.to_string()
      print "Player now occupies spaces: ", board.get_positions_of(board.player)
      print "Opponent now occupies spaces: ", board.get_positions_of(board.opponent)
      print ""
      self.players_move(board)

  # uses Minimax algorithm to return (score, space) representing 
  # the best possible next move given a board and a player.  
  def minimax(self, board, player, depth):
    all_moves = []
    for i in range (1, 10):
      all_moves.append(0)
    self.__minimax(board, player, depth, all_moves)
    best_pos = max(board.get_open_positions(), key=lambda x: all_moves[x - 1]);
    print all_moves
    return (all_moves[best_pos - 1], best_pos)

  def __minimax(self, board, player, depth, all_moves):
    if board.won_by(board.opponent):
      return -depth
    elif board.is_tied():
      return 0
    elif board.won_by(board.player):
      return depth
    else:
      best = None
      for move in board.get_open_positions():
        board.make_move(int(move), player)
        score = self.__minimax(board, board.get_enemy_of(player), depth + 1, all_moves)
        if score != None:
          all_moves[move - 1] += score
        board.make_move(int(move), str(move))
        if player == board.player:
          if score < best:
            best = score
        else:
          if score > best:
            best = score
      return best

################################# BOARD CLASS #################################

class TicTacToeBoard (object):
  def __init__(self): 
    self.player = "X"
    self.opponent = "O"
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

  def make_move(self, move, player):
    self.positions[move] = player
       
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
   
  # returns True if a spot is empty, otherwise False
  def is_taken(self, move):
    if self.positions[int(move)] != move:
      return True
    else: 
      return False  

  # checks to see if a character is a number between 1 and board.size*board.size
  # returns True if valid, False otherwise
  def is_valid_input(self, char):
    if isinstance(char, int):
      if char < 1:
        return False
      elif char > self.size*self.size:
        return False
      else:
        return True
    else:
      return False

  # takes in a board and a player and returns the winning configuration
  # if game has been won by that player, otherwise returns None
  def winning_configuration(self, player):
    # horizontal
    winningCombo = []
    j = 1
    while j <= self.size*self.size:
      winningCombo = []
      for i in range(j, j+3):
        if self.positions[i] == player:
          winningCombo.append(i)
      if len(winningCombo) == self.size:
        return winningCombo
      j = j+self.size
    # vertical
    if self.positions[1] == player and self.positions[1] == self.positions[4] and self.positions[4] == self.positions[7]:
      return [1, 4, 7]
    elif self.positions[2] == player and self.positions[2] == self.positions[5] and self.positions[5] == self.positions[8]:
      return [2, 5, 8]
    elif self.positions[3] == player and self.positions[3] == self.positions[6] and self.positions[6] == self.positions[9]:
      return [3, 6, 9]
    # diagonal
    elif self.positions[1] == player and self.positions[1] == self.positions[5] and self.positions[5] == self.positions[9]:
      return [1, 5, 9]
    # other diagonal
    elif self.positions[3] == player and self.positions[3] == self.positions[5] and self.positions[5] == self.positions[7]:
      return [3, 5, 7]
    # if no wins
    else:
      return None

  # returns the winning move if player is about to win
  def is_about_to_win(self):
    # horizontal
    if self.positions[2] == self.opponent and self.positions[2] == self.positions[3] and self.positions[1] == "1":
      return 1
    elif self.positions[1] == self.opponent and self.positions[1] == self.positions[3] and self.positions[2] == "2":
      return 2
    elif self.positions[1] == self.opponent and self.positions[1] == self.positions[2] and self.positions[3] == "3":
      return 3
    elif self.positions[5] == self.opponent and self.positions[5] == self.positions[6] and self.positions[4] == "4":
      return 4
    elif self.positions[4] == self.opponent and self.positions[4] == self.positions[6] and self.positions[5] == "5":
      return 5
    elif self.positions[4] == self.opponent and self.positions[4] == self.positions[5] and self.positions[6] == "6":
      return 6
    elif self.positions[8] == self.opponent and self.positions[8] == self.positions[9] and self.positions[7] == "7":
      return 7
    elif self.positions[7] == self.opponent and self.positions[7] == self.positions[9] and self.positions[8] == "8":
      return 8
    elif self.positions[7] == self.opponent and self.positions[7] == self.positions[8] and self.positions[9] == "9":
      return 9
    # vertical
    elif self.positions[1] == self.positions[4] == self.opponent:
      return 7
    elif self.positions[1] == self.positions[7] == self.opponent:
      return 4
    elif self.positions[4] == self.positions[7] == self.opponent:
      return 1
    elif self.positions[2] == self.positions[5] == self.opponent:
      return 8
    elif self.positions[2] == self.positions[8] == self.opponent:
      return 5
    elif self.positions[5] == self.positions[8] == self.opponent:
      return 2
    elif self.positions[3] == self.positions[6] == self.opponent:
      return 9
    elif self.positions[3] == self.positions[9] == self.opponent:
      return 6
    elif self.positions[6] == self.positions[9] == self.opponent:
      return 3
  # diagonals
    elif self.positions[1] == self.positions[9] and self.positions[1] == self.opponent :
      return 5
    elif self.positions[1] == self.positions[5] and self.positions[1] == self.opponent :
      return 9
    elif self.positions[5] == self.positions[9] and self.positions[1] == self.opponent :
      return 1
    elif self.positions[3] == self.positions[5] and self.positions[3] == self.opponent :
      return 7
    elif self.positions[3] == self.positions[7] and self.positions[3] == self.opponent :
      return 5
    elif self.positions[5] == self.positions[7] and self.positions[5] == self.opponent :
      return 3
    else:
      return None

  def won_by(self, player):
    if self.winning_configuration(player) is None:
      return False
    else:
      return True

  # takes in a board and returns True if board has been completely filled 
  # and no one has won, False otherwise
  def is_tied(self):
    if self.won_by(board.player) or self.won_by(board.opponent):
      return False
    else:
      for key in self.positions.keys():
        if self.is_taken(str(key)) is False:
          return False
      return True
     
  # takes in a board and a player and returns all spaces occupied by that player
  def get_positions_of(self, player):
    spaces = []
    for i in range (1, 10):
      if self.positions[i] == player: 
        spaces.append(i)
    return spaces

  # returns "X" if player is "O" and vice versa
  def get_enemy_of(self, player):
    if player == self.player:
      return self.opponent
    else:
      return self.player

  # takes in a board and returns all currently empty spaces
  def get_open_positions(self):
    not_spaces = []
    for i in range(1, 10):
      if self.positions[i] != self.player and self.positions[i] != self.opponent:
        not_spaces.append(int(self.positions[i]))
    return not_spaces
    
################################# SCRIPT #################################    

board = TicTacToeBoard()
board.to_string()
helper = HelperFunctions()
helper.players_move(board)