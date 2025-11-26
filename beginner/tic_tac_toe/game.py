import time
from players import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board =  self.makeBoard()# I'll use a single list to rep 3x3 board
        self.current_winner = None # keep track of winner!
        
    @staticmethod
    def makeBoard():
        return [' ' for _ in range(9)]
        
    def printBoard(self):
        # this is just getting the rows
        for row in [self.board[i*3:(i+1)] for i in range(3)]:
            print('| '+' | '.join(row) + ' |')
            
    @staticmethod
    def printBoardNums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| '+' | '.join(row) + ' |')
            
    def makeMove(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return True. If invalid, return False
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # winner if 3 in a row anywhere... i have chack all the possiblities!
        # first let's check the row
        row_inx = square // 3
        row = self.board[row_inx*3 : (row_inx+1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        # check the column
        col_inx = square % 3
        column = [self.board[col_inx+1*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # check diagonals, but only if the square is an even number (0, 2, 4, 6, 8)
        # these are the only moves possible to win a diagonal
        if square%2==0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
            
        # if all of these fails
        return False
            
        
    def emptySquares(self):
        return ' ' in self.board
    
    def numEmptySquares(self):
        # return len(self.availableMoves())
        return self.board.count(' ')
    
    def availableMoves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for (i, spot) in enumerate(self.board):
            # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
            # if spot == ' ':
                # moves.append(i)
        # return moves


            

def play(game, x_player, o_player, print_game=True):
    # return the winner of the game(the LETTER)! or None for a tie
    if print_game:
        game.printBoardNums()
        
    letter = 'X' # starting letter
    # iterate while the game still has empty squares, 
    # (I don't have to worry about winner because we'll just return that which breaks the loop)
    
    while game.emptySquares():
        # get the move from appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
            
        # defining a function to make a move!
        if game.makeMove(square, letter):
            if print_game:
                print(letter + f' make a move to square {square}')
                game.printBoard()
                print('') # just empty line
                
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
                    
                
            # after I made my move, I need to alternate letters
            letter = 'O' if letter == 'X' else 'X'
            # if letter == 'X':
            #     letter == 'O'
            # else:
            #     letter == 'X'
            
            # but WAIT! What if I WON!??
        # tiny break
        time.sleep(0.8)
            
        if print_game:
            print("It's a tie")

if __name__ == "__main__":
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)