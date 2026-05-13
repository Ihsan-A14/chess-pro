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
        self.board_arr = [['wr', 'wn', 'wb', 'wq', 'wk', 'wb','wn', 'wr'],
                     ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
                     ['--', '--', '--', '--', '--', '--', '--', '--'],
                     ['--', '--', '--', '--', '--', '--', '--', '--'],
                     ['--', '--', '--', '--', '--', '--', '--', '--'],
                     ['--', '--', '--', '--', '--', '--', '--', '--'],
                     ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
                     ['br', 'bn', 'bb', 'bq', 'bk', 'bb','bn', 'br']]
        
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
        
        return
        

chess = BoardRep()
chess.move([(1,2), (4,2)])
chess.move([(7,2), (4,2)])
chess.undo()
chess.undo()
chess.undo()



        
