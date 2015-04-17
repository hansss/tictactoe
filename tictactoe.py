# import libraries here

# Design interface of the board from http://www.leaseweblabs.com/2013/12/python-tictactoe-tk-minimax-ai/ 
# class in which game takes place
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

    # returns the board as a string
    def board_to_string(self):
        str = ''
        for j in range(self.size):
            for i in range(self.size):
                str += self.positions[i,j] + " "
            str += "\n"
        return str

################################### HELPER FUNCTIONS ##############################
#checks to see if the proposed move is a winning move and ends the game if it is
def winning(self, position):
    #pseudocode
    if not Analyze.isTaken:
        if Analyze.isWon(self, position):
            return updated board with new position marked 
             prints "Player __ won the game"
        else:
            switch users
    else:
        print "This spot is already taken"
        prompt the user to make a different move


# returns the winning configuration, if game has been won by the opponent.
# otherwise returns None

#checks to see which spots are remaining
def openPositions(self):
    op = []
    #pseudocode
    for pos in self.positions:
        if Analyze.isTaken append to recurse over the rest of the list
        else append op.append(pos)

# recursive algorithm function. takes in a player, which is either 'X' or 'O'
# and checks first to see if the game has been won or tied. Otherwise, it 
# evaluates the possible game states and returns the optimal next 
# move for the player in tuple format: (score, position)
def nextMove(board, player):
    # TODO

################################### ANALYZER CLASS #############################

#class for methods that analyze a certain move/board configuration
class Analyze:
    #checks to see if a position is already taken or not
    def isTaken(board, position):
        if position in board.positions then True
        else False


    #checks to see if a given move for a given board configuration is a winning move
    def isWon(board, position):
    # horizontal - check to see if this move results in a horizontal streak

    # vertical - check to see if this move results in a vertical streak 
    
    # forward diagonal - check to see if this move results in a forward diagonal streak 
   
    # backwards diagonal - check to see if this move results in a backwards diagonal streak 
    
    # otherwise, default
    return None

    # returns false if any one position on the board is empty, else true
    # (because if all spots on the board are filled and no one has won, it
    # is a tie)
    def isTied(board, position):
        for position in board.positions:
            if board.positions[position] == board.empty:
                return False
        return True


################################### GUI CLASS #############################
# class for user interactivity
class GUI:

