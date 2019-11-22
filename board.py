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
        self.white_piece = 15
        self.black_piece = 15
        self.side = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 5), (2, 6), (3, 7), (4, 8), (5, 7), (6, 6), (7, 5),
                     (8, 4),
                     (8, 3), (8, 2), (8, 1), (8, 0), (7, 0), (6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0)]

    def display(self):
        pass

    def insert(self, player):
        loc = input("Please input the location number,from 0 to 23: ")
        if loc < 0 or loc > 23:
            print("Illegal input, try again! ")
            return self.insert(self, player)
        else:
            self.board[self.side[loc][0]][self.side[loc][1]] = player
            if player == 1:
                self.black_piece = self.black_piece - 1
            if player == 2:
                self.white_piece = self.white_piece - 1

    def direction(self):
        for i in self.side:
            if self.board[i[0]][i[1]] != 0:
                loc_x = i[0]
                loc_y = i[1]
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

    def push(self, direction):
        for i in self.side:
            if self.board[i[0]][i[1]] != 0:
                loc_x = i[0]
                loc_y = i[1]
        # 左上到右下
        if direction == 'M' and (loc_x, loc_y) == (0, 0):
            order = [(loc_x, loc_y), (loc_x + 1, loc_y + 1), (loc_x + 2, loc_y + 2), (loc_x + 3, loc_y + 3),
                     (loc_x + 4, loc_y + 4), (loc_x + 5, loc_y + 4), (loc_x + 6, loc_y + 4), (loc_x + 7, loc_y + 4)]
            for index, obj in enumerate(order):
                if self.board[obj[0]][obj[1]] == 0:
                    while index > 0:
                        self.board[order[index][0]][order[index][1]] = self.board[order[index - 1][0]][
                            order[index - 1][1]]
                        index = index - 1
                    self.board[order[0][0]][order[0][1]] = 0
                    break
        if direction == 'L' and loc_x == 0:
            order = []
            while loc_x < 4:
                order.append((loc_x, loc_y))
                loc_x = loc_x + 1
                loc_y = loc_y + 1
            while loc_x >= 4 and loc_x < 8 and loc_y < (12 - loc_x):
                order.append((loc_x, loc_y))
                loc_x = loc_x + 1
            for index, obj in enumerate(order):
                if self.board[obj[0]][obj[1]] == 0:
                    while index > 0:
                        self.board[order[index][0]][order[index][1]] = self.board[order[index - 1][0]][
                            order[index - 1][1]]
                        index = index - 1
                    self.board[order[0][0]][order[0][1]] = 0
                    break
        # 右上到左下
        if direction == 'M' and (loc_x, loc_y) == (0, 4):
            order = [(loc_x, loc_y), (loc_x + 1, loc_y), (loc_x + 2, loc_y), (loc_x + 3, loc_y), (loc_x + 4, loc_y),
                     (loc_x + 5, loc_y - 1), (loc_x + 6, loc_y - 2), (loc_x + 7, loc_y - 3)]
            order = order[0:(loc_y + 4)]
            for index, obj in enumerate(order):
                if self.board[obj[0]][obj[1]] == 0:
                    while index > 0:
                        self.board[order[index][0]][order[index][1]] = self.board[order[index - 1][0]][
                            order[index - 1][1]]
                        index = index - 1
                    self.board[order[0][0]][order[0][1]] = 0
                    break
        if direction == 'R' and (loc_x, loc_y) == (0, 4):
            order = []
            while loc_x < 4:
                order.append((loc_x, loc_y))
                loc_x = loc_x + 1

            while loc_x >= 4 and loc_x < 8 and loc_y > 0:
                order.append((loc_x, loc_y))
                loc_x = loc_x + 1
                loc_y = loc_y - 1
            for index, obj in enumerate(order):
                if self.board[obj[0]][obj[1]] == 0:
                    while index > 0:
                        self.board[order[index][0]][order[index][1]] = self.board[order[index - 1][0]][
                            order[index - 1][1]]
                        index = index - 1
                    self.board[order[0][0]][order[0][1]] = 0
                    break
        # 左下到右上
        if direction == 'M' and (loc_x, loc_y) == (8, 0):
            order = [(loc_x, loc_y), (loc_x - 1, loc_y + 1), (loc_x - 2, loc_y + 2), (loc_x - 3, loc_y + 3),
                     (loc_x - 4, loc_y + 4), (loc_x - 5, loc_y + 4), (loc_x - 6, loc_y + 4), (loc_x - 7, loc_y + 4)]
            for index, obj in enumerate(order):
                if self.board[obj[0]][obj[1]] == 0:
                    while index > 0:
                        self.board[order[index][0]][order[index][1]] = self.board[order[index - 1][0]][
                            order[index - 1][1]]
                        index = index - 1
                    self.board[order[0][0]][order[0][1]] = 0
                    break
        if direction == 'R' and loc_x == 8:
            order = []
            while loc_x > 4:
                order.append((loc_x, loc_y))
                loc_x = loc_x - 1
                loc_y = loc_y + 1
            while loc_x <= 4 and loc_x > 0 and loc_y < loc_x + 4:
                order.append((loc_x, loc_y))
                loc_x = loc_x - 1
            for index, obj in enumerate(order):
                if self.board[obj[0]][obj[1]] == 0:
                    while index > 0:
                        self.board[order[index][0]][order[index][1]] = self.board[order[index - 1][0]][
                            order[index - 1][1]]
                        index = index - 1
                    self.board[order[0][0]][order[0][1]] = 0
                    break

        # 右下到左上
        if direction == 'M' and (loc_x, loc_y) == (8, 4):
            order = [(loc_x, loc_y), (loc_x - 1, loc_y), (loc_x - 2, loc_y), (loc_x - 3, loc_y), (loc_x - 4, loc_y),
                     (loc_x - 5, loc_y - 1), (loc_x - 6, loc_y - 2), (loc_x - 7, loc_y - 3)]
            for index, obj in enumerate(order):
                if self.board[obj[0]][obj[1]] == 0:
                    while index > 0:
                        self.board[order[index][0]][order[index][1]] = self.board[order[index - 1][0]][
                            order[index - 1][1]]
                        index = index - 1
                    self.board[order[0][0]][order[0][1]] = 0
                    break
        if direction == 'L' and loc_x == 8:
            order = []
            while loc_x > 4:
                order.append((loc_x, loc_y))
                loc_x = loc_x - 1

            while loc_x <= 4 and loc_x > 0 and loc_y > 0:
                order.append((loc_x, loc_y))
                loc_x = loc_x - 1
                loc_y = loc_y - 1
            for index, obj in enumerate(order):
                if self.board[obj[0]][obj[1]] == 0:
                    while index > 0:
                        self.board[order[index][0]][order[index][1]] = self.board[order[index - 1][0]][
                            order[index - 1][1]]
                        index = index - 1
                    self.board[order[0][0]][order[0][1]] = 0
                    break

        # 从左到右
        if direction == 'M' and (loc_x, loc_y) == (4, 0):
            order = [(loc_x, loc_y), (loc_x, loc_y + 1), (loc_x, loc_y + 2), (loc_x, loc_y + 3), (loc_x, loc_y + 4),
                     (loc_x, loc_y + 5), (loc_x, loc_y + 6), (loc_x, loc_y + 7)]
            for index, obj in enumerate(order):
                if self.board[obj[0]][obj[1]] == 0:
                    while index > 0:
                        self.board[order[index][0]][order[index][1]] = self.board[order[index - 1][0]][
                            order[index - 1][1]]
                        index = index - 1
                    self.board[order[0][0]][order[0][1]] = 0
                    break
        if direction == 'R' and loc_y == 0:

            order = [(loc_x, loc_y), (loc_x, loc_y + 1), (loc_x, loc_y + 2), (loc_x, loc_y + 3), (loc_x, loc_y + 4),
                     (loc_x, loc_y + 5), (loc_x, loc_y + 6), (loc_x, loc_y + 7)]
            order = order[0:(min(loc_x, 8 - loc_x) + 4)]
            for index, obj in enumerate(order):
                if self.board[obj[0]][obj[1]] == 0:
                    while index > 0:
                        self.board[order[index][0]][order[index][1]] = self.board[order[index - 1][0]][
                            order[index - 1][1]]
                        index = index - 1
                    self.board[order[0][0]][order[0][1]] = 0
                    break

        # 从右到左
        if direction == 'M' and (loc_x, loc_y) == (4, 8):
            order = [(loc_x, loc_y), (loc_x, loc_y - 1), (loc_x, loc_y - 2), (loc_x, loc_y - 3), (loc_x, loc_y - 4),
                     (loc_x, loc_y - 5), (loc_x, loc_y - 6), (loc_x, loc_y - 7)]
            for index, obj in enumerate(order):
                if self.board[obj[0]][obj[1]] == 0:
                    while index > 0:
                        self.board[order[index][0]][order[index][1]] = self.board[order[index - 1][0]][
                            order[index - 1][1]]
                        index = index - 1
                    self.board[order[0][0]][order[0][1]] = 0
                    break
        if direction == 'L' and loc_y == min(loc_x, 8 - loc_x) + 4:
            order = [(loc_x, loc_y), (loc_x, loc_y - 1), (loc_x, loc_y - 2), (loc_x, loc_y - 3), (loc_x, loc_y - 4),
                     (loc_x, loc_y - 5), (loc_x, loc_y - 6), (loc_x, loc_y - 7)]
            order = order[0:(min(loc_x, 8 - loc_x) + 4)]
            for index, obj in enumerate(order):
                if self.board[obj[0]][obj[1]] == 0:
                    while index > 0:
                        self.board[order[index][0]][order[index][1]] = self.board[order[index - 1][0]][
                            order[index - 1][1]]
                        index = index - 1
                    self.board[order[0][0]][order[0][1]] = 0
                    break

    def update(self):
        # remove piece if possible
        upleft = [(3, 0), (2, 0), (1, 0), (0, 0), (0, 1), (0, 2), (0, 3)]
        upright = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 5), (2, 6), (3, 7)]
        downleft = [(5, 0), (6, 0), (7, 0), (8, 0), (8, 1), (8, 2), (8, 3)]
        downright = [(8, 1), (8, 2), (8, 3), (8, 4), (7, 5), (6, 6), (5, 7)]
        left = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
        right = [(1, 5), (2, 6), (3, 7), (4, 8), (5, 7), (6, 6), (7, 5)]

        self.white_piece = 15
        self.black_piece = 15

        for i in upleft:
            loc_x = i[0]
            loc_y = i[1]
            black_number = 0
            white_number = 0
            order = []
            while loc_x < 4:
                order.append((loc_x, loc_y))
                loc_x = loc_x + 1
                loc_y = loc_y + 1
            while loc_x >= 4 and loc_x < 8 and loc_y < (12 - loc_x):
                order.append((loc_x, loc_y))
                loc_x = loc_x + 1
            for j in order:
                if self.board[j[0]][j[1]] == 1:
                    black_number = black_number + 1
                if self.board[j[0]][j[1]] == 2:
                    white_number = white_number + 1
            if white_number >= 4:
                self.white_piece = white_number + self.white_piece
                for m in order:
                    self.board[m[0]][m[1]] = 0
            if black_number >= 4:
                self.black_piece = black_number + self.black_piece
                for m in order:
                    self.board[m[0]][m[1]] = 0

        for i in upright:
            loc_x = i[0]
            loc_y = i[1]
            black_number = 0
            white_number = 0
            order = []
            while loc_x < 4:
                order.append((loc_x, loc_y))
                loc_x = loc_x + 1
            while loc_x >= 4 and loc_x < 8 and loc_y > 0:
                order.append((loc_x, loc_y))
                loc_x = loc_x + 1
                loc_y = loc_y - 1
            for j in order:
                if self.board[j[0]][j[1]] == 1:
                    black_number = black_number + 1
                if self.board[j[0]][j[1]] == 2:
                    white_number = white_number + 1
            if white_number >= 4:
                self.white_piece = white_number + self.white_piece
                for m in order:
                    self.board[m[0]][m[1]] = 0
            if black_number >= 4:
                self.black_piece = black_number + self.black_piece
                for m in order:
                    self.board[m[0]][m[1]] = 0

        for i in downleft:
            loc_x = i[0]
            loc_y = i[1]
            black_number = 0
            white_number = 0
            order = []
            while loc_x > 4:
                order.append((loc_x, loc_y))
                loc_x = loc_x - 1
                loc_y = loc_y + 1
            while loc_x <= 4 and loc_x > 0 and loc_y < loc_x + 4:
                order.append((loc_x, loc_y))
                loc_x = loc_x - 1
            for j in order:
                if self.board[j[0]][j[1]] == 1:
                    black_number = black_number + 1
                if self.board[j[0]][j[1]] == 2:
                    white_number = white_number + 1
            if white_number >= 4:
                self.white_piece = white_number + self.white_piece
                for m in order:
                    self.board[m[0]][m[1]] = 0
            if black_number >= 4:
                self.black_piece = black_number + self.black_piece
                for m in order:
                    self.board[m[0]][m[1]] = 0

        for i in downright:
            loc_x = i[0]
            loc_y = i[1]
            black_number = 0
            white_number = 0
            order = []
            while loc_x > 4:
                order.append((loc_x, loc_y))
                loc_x = loc_x - 1
            while loc_x <= 4 and loc_x > 0 and loc_y > 0:
                order.append((loc_x, loc_y))
                loc_x = loc_x - 1
                loc_y = loc_y - 1
            for j in order:
                if self.board[j[0]][j[1]] == 1:
                    black_number = black_number + 1
                if self.board[j[0]][j[1]] == 2:
                    white_number = white_number + 1
            if white_number >= 4:
                self.white_piece = white_number + self.white_piece
                for m in order:
                    self.board[m[0]][m[1]] = 0
            if black_number >= 4:
                self.black_piece = black_number + self.black_piece
                for m in order:
                    self.board[m[0]][m[1]] = 0

        for i in left:
            loc_x = i[0]
            loc_y = i[1]
            black_number = 0
            white_number = 0
            order = [(loc_x, loc_y), (loc_x, loc_y + 1), (loc_x, loc_y + 2), (loc_x, loc_y + 3), (loc_x, loc_y + 4),
                     (loc_x, loc_y + 5), (loc_x, loc_y + 6), (loc_x, loc_y + 7)]
            order = order[0:(min(loc_x, 8 - loc_x) + 4)]
            for j in order:
                if self.board[j[0]][j[1]] == 1:
                    black_number = black_number + 1
                if self.board[j[0]][j[1]] == 2:
                    white_number = white_number + 1
            if white_number >= 4:
                self.white_piece = white_number + self.white_piece
                for m in order:
                    self.board[m[0]][m[1]] = 0
            if black_number >= 4:
                self.black_piece = black_number + self.black_piece
                for m in order:
                    self.board[m[0]][m[1]] = 0

        for i in right:
            loc_x = i[0]
            loc_y = i[1]
            black_number = 0
            white_number = 0
            order = [(loc_x, loc_y), (loc_x, loc_y - 1), (loc_x, loc_y - 2), (loc_x, loc_y - 3), (loc_x, loc_y - 4),
                     (loc_x, loc_y - 5), (loc_x, loc_y - 6), (loc_x, loc_y - 7)]
            order = order[0:(min(loc_x, 8 - loc_x) + 4)]
            for j in order:
                if self.board[j[0]][j[1]] == 1:
                    black_number = black_number + 1
                if self.board[j[0]][j[1]] == 2:
                    white_number = white_number + 1
            if white_number >= 4:
                self.white_piece = white_number + self.white_piece
                for m in order:
                    self.board[m[0]][m[1]] = 0
            if black_number >= 4:
                self.black_piece = black_number + self.black_piece
                for m in order:
                    self.board[m[0]][m[1]] = 0

    def gameover(self):
        if self.white_piece == 0:
            print("Game is Over, Black wins!")
            return True
        if self.black_piece == 0:
            print("Game is over, White wins!")
            return True
        else:
            print("Game goes on!")
            return False
        
if __name__== "__main__":
    game = board()
    while not game.gameover():
        n = 1
        if n%2 != 0:
            game.insert(1)
        else:
            game.insert(2)
        n = n+1
        direction = game.direction()
        game.push(direction)
        game.update()
        # 改这个
        print(game.board.tolist())   
