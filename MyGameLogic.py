'''
Author: Eric P. Nichols
Date: Feb 8, 2008.
Board class.
Board data:
  1=white, -1=black, 0=empty
  first dim is column , 2nd is row:
     pieces[1][7] is the square in column 2,
     at the opposite end of the board in row 8.
Squares are stored and manipulated as (x,y) tuples.
x is the column, y is the row.
'''
class Board():

    # list of all 8 directions on the board, as (x,y) offsets
    __directions = [(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]

    def __init__(self, n):
        "Set up initial board configuration."

        self.n = n
        # Create the empty board array.
        self.pieces = [None]*self.n
        for i in range(self.n):
            self.pieces[i] = [0]*self.n

        # Set up the initial 4 pieces.
        '''self.pieces[0][0] = -1
        self.pieces[0][1] = -1
        self.pieces[1][0] = -1;
        ''''self.pieces[int(self.n/2)][int(self.n/2)] = -1;'''
        
        

    # add [][] indexer syntax to the Board
    def __getitem__(self, index): 
        return self.pieces[index]

    def countDiff(self, color):
        """Counts the # pieces of the given color
        (1 for white, -1 for black, 0 for empty spaces)"""
        count = 0
        for y in range(self.n):
            for x in range(self.n):
                if self[x][y]==color:
                    count += 1
                if self[x][y]==-color:
                    count -= 1
        return count

    def get_legal_moves(self, color):
        """Returns all the legal moves for the given color.
        (1 for white, -1 for black
        """
        moves = set()  # stores the legal moves.

        moves = []
        for i in range( self.n):
            for j in range( self.n):
                if self[i][j] ==0:
                     moves.append((i,j))   
        
        # return the generated move list
        return moves

    def has_legal_moves(self, color):
        return len(self.get_legal_moves(color) ) > 0


       

    def execute_move(self, move, color):
        """Perform the given move on the board; flips pieces as necessary.
        color gives the color pf the piece to play (1=white,-1=black)
        """

        x0,y0 = move
        
        '''for x in range( self.n):
            for y in range( self.n):
                if x == x0 or y == y0 or abs(x-x0) == abs(y-y0):
                    if max(abs(x-x0),abs(y-y0)) < 3:
                        self[x][y] *= -1'''
                        
                        
        for u in self.__directions:
            dx, dy = u
            for k in range(1,self.n):
                x,y = x0 + k*dx, y0 + k*dy
                if x<0 or y<0 or x>= self.n or y >= self.n or self[x][y] == 0:
                    break
                self[x][y] *= -1       

       
        self[x0][y0] = color
   

