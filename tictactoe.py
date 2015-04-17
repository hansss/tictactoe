# import libraries here

# class in which game takes place
class Board:

    # initializer
    def __init__(self):
        self.player = 'X' # player starts as X
        self.opponent = 'O' 
        self.empty = '_' # empty spaces are denoted by underscores _
        self.size = 3 # default board size 3x3
        self.positions = {} # 2D array of board positions
        for j in range(self.size):
            for i in range(self.size):
                self.positions[i,j] = self.empty # initialize all positions to empty

    # returns the board as a string
    def board_to_string(self):
        str = ''
        for j in range(self.size):
            for i in range(self.size):
                str += self.positions[i,j] + " "
            str += "\n"
        return str

################################### HELPER FUNCTIONS ##############################

# returns the winning configuration, if game has been won by the opponent.
# otherwise returns None
def isWon(board):
    # horizontal
    for j in range(board.size):
        winning_config = []
        for i in range(board.size):
            if board.positions[i,j] == board.opponent:
                winning_config.append((i,j))
            if len(winning_config) == board.size:
                return winning_config
    # vertical
    for i in range(board.size):
        winning_config = []
        for j in range(board.size):
            if board.positions[i,j] == board.opponent:
                winning_config.append((i,j))
            if len(winning_config) == board.size:
                return winning_config
    # forward diagonal
    winning_config = []
    for j in range(board.size):
        i = j
        if board.positions[i,j] == board.opponent:
            winning_config.append((i,j))
        if len(winning_config) == board.size:
            return winning_config
    # backwards diagonal
    winning_config = []
    for j in range(board.size):
        i = board.size - 1 - j
        if board.positions[i,j] == board.opponent:
            winning_config.append((i,j))
        if len(winning_config) == board.size:
            return winning_config
    # otherwise, default
    return None

# returns false if any one position on the board is empty, else true
# (because if all spots on the board are filled and no one has won, it
# is a tie)
def isTied(board):
    for (i,j) in board.positions:
        if board.positions[i,j] == board.empty:
            return False
    return True

# recursive algorithm function. takes in a player, which is either 'X' or 'O'
# and checks first to see if the game has been won or tied. Otherwise, it 
# evaluates the possible game states and returns the optimal next 
# move for the player in tuple format: (score, position)
def nextMove(board, player):
    # TODO

# class for user interactivity
class GUI:

