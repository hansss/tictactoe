# import libraries here

# class in which game takes places
class Board:

    # initializer
    def __init__(self):
        self.player = 'X' # by default, player is X
        self.computer = 'O' # computer opponent is O
        self.empty = '_' # empty spaces are denoted by underscores _
        self.size = 3 # default board size 3x3
        self.positions = {} # 2D array of board positions
        for j in range(self.size):
            for i in range(self.size):
                self.positions[i,j] = self.empty # initialize all positions to empty
            
    # executes a move in position (x,y) on the board        
    def move(self, x, y):
        board = Board(self) # get board
        board.positions[x,y] = board.player # marks position (x,y) with X or O depending on who is playing
        (board.player, board.computer) = (board.computer, board.player) # switches players' turns
        return board # return updated board

    # algorithmic function. takes in a boolean value, player, which determines
    # whose turn it is, and checks first to see if the game has been won or tied.
    # Otherwise, it evaluates the possible game states and returns the optimal next 
    # move for the player.
    def __minimax(self, player):
        # TODO

    # returns the best possible position for a given player on its turn
    def best(self):
        return self.__minimax(True)[1]

    # returns the winning configuration, if game has been won
    def won(self):
        # horizontal
        for j in range(self.size):
            winning_config = []
            for i in range(self.size):
                if self.positions[i,j] == self.computer:
                    winning_config.append((i,j))
                if len(winning_config) == self.size:
                    return winning_config
        # vertical
        for i in range(self.size):
            winning_config = []
            for j in range(self.size):
                if self.positions[i,j] == self.computer:
                    winning_config.append((i,j))
                if len(winning_config) == self.size:
                    return winning_config
        # forward diagonal
        winning_config = []
        for j in range(self.size):
            i = j
            if self.positions[i.j] == self.computer:
                winning_config.append((i,j))
            if len(winning_config) == self.size:
                return winning_config
        # backwards diagonal
        winning_config = []
        for j in range(self.size):
            i = self.size - 1 - j
            if self.positions[i.j] == self.computer:
                winning_config.append((i,j))
            if len(winning_config) == self.size:
                return winning_config
        # otherwise, default
        return None

    # returns the board as a string
    def board_to_string(self):
        str = ''
        for j in range(self.size):
            for i in range(self.size):
                str += self.positions[i,j] + " "
            str += "\n"
        return str