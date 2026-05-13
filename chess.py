import pygame

class BoardRep:
    def __init__(self):
        board_arr = [['wr', 'wk', 'wb', 'wq', 'wk', 'wb','wk', 'wr'],
                     ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
                     ['--', '--', '--', '--', '--', '--', '--', '--'],
                     ['--', '--', '--', '--', '--', '--', '--', '--'],
                     ['--', '--', '--', '--', '--', '--', '--', '--'],
                     ['--', '--', '--', '--', '--', '--', '--', '--'],
                     ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
                     ['br', 'bk', 'bb', 'bq', 'bk', 'bb','bk', 'br']]
        
        white_move = True #If true then white's turn else black's turn


        
