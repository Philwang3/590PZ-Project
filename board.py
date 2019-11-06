"""
First version of GIPF, using ndarray
May switch to networkx later
"""

import numpy as np


class board:

    def __init__(self):
        self.board = np.array([[0, 0, 0, 0, 0],
                               [0, 2, 0, 0, 1, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 2, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [0, 2, 0, 0, 1, 0],
                               [0, 0, 0, 0, 0]])

    def display(self):
        pass

    def insert(self, loc_x, loc_y, player):
        if loc_x != 0 and loc_x != 8 and loc_y != 0 and loc_y != min((8 - loc_x), loc_x) + 4:
            print("Illegal input, try again! ")
            return False
        else:
            self.board[loc_x][loc_y] = player

    def direction(self, loc_x, loc_y):
        if (loc_x == 0 and loc_y == 0) or \
                (loc_x == 0 and loc_y == 4) or \
                (loc_x == 4 and loc_y == 0) or \
                (loc_x == 4 and loc_y == 8) or \
                (loc_x == 8 and loc_y == 0) or \
                (loc_x == 8 and loc_y == 4):

            direction = 'M'
        else:
            direction = input("Please choose your direction: L or R: ")

        return direction

    def update(self, direction):
        if direction == 'L':
            pass
        if direction == 'R':
            pass
        if direction == 'M':
            pass


class player:

    def __init__(self):
        self.id = 1
        self.count = 15

    def display(self):
        pass

    def update(self):
        pass


def play():
    pass