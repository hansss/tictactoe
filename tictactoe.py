# import libraries here

# Design interface of the board from http://www.leaseweblabs.com/2013/12/python-tictactoe-tk-minimax-ai/ 
# class in which game takes place

################################### BOARD CLASS ##############################
class Board:

    # initializer
    def __init__(self):
        self.player = 'X' # player starts as X
        self.opponent = 'O' 
        self.empty = '_' # empty spaces are denoted by underscores _
        self.size = 3 # default board size 3x3
        self.positions = {} # 2D array of board positions
        self.takenPositions = []
        for j in range(self.size):
            for i in range(self.size):
                self.positions[i,j] = self.empty # initialize all positions to empty

    # returns the board as a string, good for debugging
    def board_to_string(self):
        str = ''
        for j in range(self.size):
            for i in range(self.size):
                str += self.positions[i,j] + " "
            str += "\n"
        return str

    # Minimax algorithm function. takes in a player, which is either 'X' or 'O'
    # and checks first to see if the game has been won or tied. Otherwise, it 
    # evaluates the possible game states and returns the optimal next 
    # move for the player in tuple format: (score, position)
    def bestMove(self, player):
        # first, check if game has already been won
        if Analyze.isWonBy(self, player):
            return (+1, None) # we win: +1 point
        elif Analyze.isWonBy(self, enemy_of(player)):
            return (-1, None) # we lose: -1 point
        # next, check if game has been tied
        elif Analyze.isTied(self):
            return (0, None) # tie: 0, no further moves
        # otherwise, use minimax to recursively figure out the best move
        else:
            # TODO

################################### HELPER FUNCTIONS ##############################

# checks to see which spots are remaining
def open_positions(board):
    spaces = []
    for i in range(board.size):
        for j in range(board.size):
            if board.positions[i,j] == board.empty:
                spaces.append((i,j))
    return spaces

# takes in a board and player and returns all spaces occupied by that player
def get_positions_of(board, player):
    spaces = []
    for i in range(board.size):
        for j in range(board.size):
            if board.positions[i,j] == player:
                spaces.append((i,j))
    return spaces

# takes in a board, a pair of x-y coordinates and a player marker (‘X’ or ‘O’), and returns the updated board with that spot filled.
def make_move(board, i, j, player):
    board.positions[i,j] = player
    return board

# if X, returns O, and vice versa
def enemy_of(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'

################################### ANALYZER CLASS #############################

# class for methods that analyze a certain move/board configuration
class Analyze:

    # checks to see if the proposed move is a winning move and ends the game if it is
    def isWinningMove(board, i, j):
    #pseudocode
    if not Analyze.isTaken:
        if Analyze.isWonBy(make_move(board, i, j, player), player):
            return make_move(board, i, j, player)
            print "Player __ won the game"
        else:
            switch users
    else:
        print "This spot is already taken"
        prompt the user to make a different move

    # checks to see if a position is already taken or not
    def isTaken(board, i, j):
        if board.positions[i,j] != board.empty:
            return True
        else False

    # checks to see board has already been won by player, and if so, returns
    # that winning configuration
    def isWonBy(board, player):
    # check all horizontal rows
    for j in range(self.size):
        winning_config = []
        for i in range(self.size):
            if self.positions[i,j] == player:
                winning_config.append((i,j))
            if len(winning_config) == self.size:
                return winning_config
    # check all vertical columns
    for i in range(self.size):
        winning_config = []
        for j in range(self.size):
            if self.positions[i,j] == player:
                winning_config.append((i,j))
            if len(winning_config) == self.size:
                return winning_config
    # check the forward diagonal
    winning_config = []
    for j in range(self.size):
        i = j
        if self.positions[i,j] == player:
            winning_config.append((i,j))
        if len(winning_config) == self.size:
            return winning_config
    # check the backwards diagonal
    winning_config = []
    for j in range(self.size):
        i = self.size - 1 - j
        if self.positions[i,j] == player:
            winning_config.append((i,j))
        if len(winning_config) == self.size:
            return winning_config
    # otherwise, default
    return None

    # returns false if any one position on the board is empty, else true
    # (because if all spots on the board are filled and no one has won, it
    # is a tie)
    def isTied(board):
        if len(open_positions(board)) == 0:
            return True
        else:
            return False

################################### GUI CLASS #############################
# class for user interactivity
class GUI:
    #TODO
