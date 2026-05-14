import pygame

class BoardRep:
    def __init__(self):
        '''
        this will construct the attributes requires for the class BoardRep

        attributes
        board_arr = stores the current chess board. starts from a defult position
        white_move = stores whose turn it is - True then white's turn else black's turn
        move_log = stores all the move done so that moves can be undone if needed
        '''
        self.board_arr = [['br', 'bn', 'bb', 'bq', 'bk', 'bb','bn', 'br'],
                     ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
                     ['--', '--', '--', '--', '--', '--', '--', '--'],
                     ['--', '--', '--', '--', '--', '--', '--', '--'],
                     ['--', '--', '--', '--', '--', '--', '--', '--'],
                     ['--', '--', '--', '--', '--', '--', '--', '--'],
                     ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
                     ['wr', 'wn', 'wb', 'wq', 'wk', 'wb','wn', 'wr']]
        
        self.white_move = True #If true then white's turn else black's turn

        self.move_log = []

        print(self.board_arr)

        return

    def move(self, info):
        '''
        move is method of class BoardRep that takes some info regarding the positions of moved piece and
        updates the backend board to reflect it as well as storing it in the log.

        parameters
        self - instance of class
        info - list of tuples. Format should be [([(start.x, start.y), (end.x, end.y))]

        returns
        None

        Side Effects
        - boardRep and move_log is modified, and white_move is changed
        '''
        start = info[0]
        end = info[1]
        info.extend((self.board_arr[start[0]][start[1]], self.board_arr[end[0]][end[1]]))

        self.board_arr[end[0]][end[1]] = info[2]

        self.board_arr[start[0]][start[1]] = '--'

        self.move_log.append(info)

        if info[2][0] == 'w':
            self.white_move = False
        else:
            self.white_move = True
        
        print(self.board_arr, self.move_log)
        return
    
    def undo(self):
        '''
        undo is a method of class BoardRep that'll undo any moves done so far

        parameters
        self
        
        returns
        None

        Side-effects
        modifies board_arr such that it becomes the previous version; deletes the last entry of move_log
        and gives the turn back 
        '''
        if len(self.move_log) == 0:
            print("no moves recorded")
            return
        last_mov = self.move_log[-1]
        start = last_mov[0]
        end = last_mov[1]
        self.board_arr[start[0]][start[1]] = last_mov[2]
        self.board_arr[end[0]][end[1]] = last_mov[3]
        self.move_log.pop()
        print(self.board_arr, self.move_log)

        if last_mov[2][0] == 'w':
            self.white_move = True
        else:
            self.white_move = False

        return None
    
    def knight_moves(self, spos):
        '''
        knight_moves is a helper function that finds all the L shaped moves knight makes and making sure the moves 
        are valid ,i.e., it exist inside the chessboard and no other piece of same color exist

        parameter
        self
        spos - starting position of knight

        returns
        None

        side effect
        add all possible positions in the list moves
        '''
        jumps = [(-2, 1), (-2, -1), (2, 1), (2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2)]
        for i in jumps:
            epos = (spos[0] + i[0], spos[1] + i[1])
            if epos[0] < 0 or epos[0] > 7 or epos[1] < 0 or epos[1] > 7:
                continue
            if self.board_arr[epos[0]][epos[1]][0] == self.board_arr[spos[0]][spos[1]][0]:
                continue
            self.moves.append([spos, epos])
        return None
    
    def slider_moves(self, spos, vec):
        '''
        slider_moves is a helper function that finds all the  moves a slider piece such as queen, rook, or bishop
        makes and making sure the moves  are valid ,i.e., it exist inside the chessboard and 
        no other piece of same color exist

        parameter
        self
        spos - starting position of piece
        vec - list of possible side to which the piece can move to


        returns
        None

        side effect
        add all possible positions in the list moves
        '''
        for i in vec:
            for j in range(1, 8):
                epos = (spos[0] + i[0] * j, spos[1] + i[1] * j)
                if epos[0] > 7 or epos[0] < 0 or epos[1] > 7 or epos[1] < 0:
                    break
                if self.board_arr[epos[0]][epos[1]][0] == self.board_arr[spos[0]][spos[1]][0]:
                    break
                if self.board_arr[epos[0]][epos[1]][0] == 'w' or self.board_arr[epos[0]][epos[1]][0] == 'b':
                    self.moves.append([spos, epos])
                    break    
                self.moves.append([spos, epos])
                
        return None
    
    def pawn_moves(self, spos):
        '''
        pawn_moves is a helper function that finds all the moves pawn makes and making sure the moves 
        are valid ,i.e., it exist inside the chessboard and no other piece of same color exist
        it checks the following:
         - if the square in front of it is free
         - if its at beginning square, then if 2 squares in front of it is free
         - if there is a opposing piece in diagonal square in front of it can it capture

        parameter
        self
        spos - starting position of knight

        returns
        None

        side effect
        add all possible positions in the list moves
        '''
        if self.white_move == True:
            dpos1 = (spos[0] - 1, spos[1] + 1)
            dpos2 = (spos[0] - 1, spos[1] - 1)
            if not(dpos1[0] > 7 or dpos1[0] < 0 or dpos1[1] > 7 or dpos1[1] < 0):
                if self.board_arr[dpos1[0]][dpos1[1]][0] == 'b':
                    self.moves.append([spos, dpos1])
            if not(dpos2[0] > 7 or dpos2[0] < 0 or dpos2[1] > 7 or dpos2[1] < 0):
                if self.board_arr[dpos2[0]][dpos2[1]][0] == 'b':
                    self.moves.append([spos, dpos2])



            epos1 = (spos[0] - 1, spos[1])
            if self.board_arr[epos1[0]][epos1[1]] != '--':
                return None
            self.moves.append([spos, epos1])

            if spos[0] == 6:
                epos2 = (spos[0] - 2, spos[1]) 
                if self.board_arr[epos2[0]][epos2[1]] != '--':
                    return None              
                self.moves.append([spos, epos2])
        
        if self.white_move == False:
            if self.board_arr[spos[0] + 1][spos[1] + 1][0] == 'b':
                self.moves.append([spos, (spos[0] + 1, spos[1] + 1)])
            epos1 = (spos[0] + 1, spos[1])
            if self.board_arr[epos1[0]] != '--':
                return None
            self.moves.append([spos, epos1])
            if spos[0] == 6:
                epos2 = (spos[0] + 2, spos[1]) 
                if self.board_arr[epos2[0]] != '--':
                    return None
                self.moves.append([spos, epos2])
            
        return None
    
    def king_moves(self, spos):
        '''
        king_moves is a helper function that checks all the boxes around the king and making sure the moves 
        are valid ,i.e., it exist inside the chessboard and no other piece of same color exist

        parameter
        self
        spos - starting position of knight

        returns
        None

        side effect
        add all possible positions in the list moves
        '''
        vec = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for i in vec:
            epos = (spos[0] + i[0], spos[1] + i[1])
            if epos[0] > 7 or epos[0] < 0 or epos[1] > 7 or epos[1] < 0:
                continue
            if self.board_arr[epos[0]][epos[1]][0] == self.board_arr[spos[0]][spos[1]][0]:
                continue
            self.moves.append([spos, epos])
    
    def get_all_moves(self):
        '''
        get_all_moves finds all possible moves of piece whose turn it is. it finds all position barring position where
        another piece of the same color exists

        parameter
        self

        returns


        '''
        self.moves = []
        for i in range(8):
            for j in range(8):
                piece = self.board_arr[i][j]
                if piece == '--':
                    continue
                if piece[0] == 'w' and self.white_move == False:
                    continue
                if piece[0] == 'b' and self.white_move == True:
                    continue
                
                if piece[1] == 'p':
                    self.pawn_moves((i, j))
                    continue

                if piece[1] == 'n':
                    self.knight_moves((i, j))
                    continue

                if piece[1] == 'r':
                    r_vec = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    self.slider_moves((i, j), r_vec)
                    continue

                if piece[1] == 'b':
                    b_vec = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
                    self.slider_moves((i, j), b_vec)
                    continue

                if piece[1] == 'q':
                    q_vec = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
                    self.slider_moves((i, j), q_vec)
                    continue
                    
                if piece[1] == 'k':
                    self.king_moves((i, j))
                    continue

                
        return self.moves


chess = BoardRep()

# Ask the engine to find every move White can make right now
moves = chess.get_all_moves()

# Print the results
print(f"Total moves found: {len(moves)}")
for move in moves:
    print(move)      
'''
chess = BoardRep()
chess.move([(1,2), (4,2)])
chess.move([(7,2), (4,2)])
chess.undo()
chess.undo()
chess.undo()'''



        
