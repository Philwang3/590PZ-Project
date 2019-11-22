import math
import pygame


class playboard():

    def __init__(self, board, window):
        x, y = self.window.get_size()
        self.size_x = 0.6 * x
        self.size_y = 0.6 * y
        self.height = 0.8 * 0.6 * y
        self.board = board
        self.window = window

    def Draw_board(self):
        self._Draw_B()
        self._DrawPieces()

    def Display_Size(self, row: int, col: int):
        row_size = (row - 4) * (self.height * math.sqrt(3) / 16)
        col_size = -(col - 4) * self.height / 8 - abs(row - 4) * (self.height / 16)
        return int(row_size + self.size_x), int(col_size + self.size_y)

    def GetButtonRadius(self):
        return int(self.height / 48)

    def GetPieceRadius(self):
        return int(self.height / 24)

    def _Draw_B(self):

        def DrawLine(angle):
            button_radius = self.GetButtonRadius()
            for i in range(1, 8):
                row_size = (i - 4) * (self.height * math.sqrt(3) / 16)
                col_size = self.height / 2 - abs(i - 4) * (self.height / 16)
                sin = math.sin(angle)
                cos = math.cos(angle)
                pos1 = [cos * row_size - sin * (-col_size), sin * row_size + cos * (-col_size)]
                pos2 = [cos * row_size - sin * (col_size), sin * row_size + cos * (col_size)]
                pos1[0] = int(pos1[0] + self.size_x)
                pos2[0] = int(pos2[0] + self.size_x)
                pos1[1] = int(pos1[1] + self.size_y)
                pos2[1] = int(pos2[1] + self.size_y)

                pygame.draw.line(self.window, (255, 255, 255), pos1, pos2)
                pygame.draw.circle(self.window, (255, 255, 255), pos1, button_radius)
                pygame.draw.circle(self.window, (255, 255, 255), pos2, button_radius)

        DrawLine(0)
        DrawLine(math.pi / 3)
        DrawLine(-math.pi / 3)

    def _DrawPieces(self):
        for row in range(9):
            for col in range(len(self.board.board[row])):
                color = self.board.board[row][col]
                if color:
                    pr = self.GetPieceRadius()
                    size = self.Display_Size(row, col)
                    if color == 1:
                        pygame.draw.circle(self.window, (255, 255, 255), size, pr, 1)
                        pygame.draw.circle(self.window, (0, 0, 0), size, pr - 1)
                    elif color == 2:
                        pygame.draw.circle(self.window, (0, 0, 0), size, pr, 1)
                        pygame.draw.circle(self.window, (255, 255, 255), size, pr - 1)


class MouseMotion_Board(object):

    def __init__(self, play_board, window):
        self.play_board = play_board
        self.window = window
        self.Button_pos = []
        for i in range(9):
            self.Button_pos.append(((i, 0), play_board.Display_Size(i, 0)))
            self.Button_pos.append(((i, 8 - abs(i - 4)), play_board.Display_Size(i, 8 - abs(i - 4))))
        for i in range(1, 4):
            self.Button_pos.append(((0, i), play_board.Display_Size(0, i)))
            self.Button_pos.append(((8, i), play_board.Display_Size(8, i)))
        self.last_fill = None

    def MouseMotion(self, pos):
        button_radius = self.play_board.GetButtonRadius()
        current_fill = None
        for button in self.Button_pos:
            dist2 = (pos[0] - button[1][0]) * (pos[0] - button[1][0]) + (pos[1] - button[1][1]) * (pos[1] - button[1][1])
            if dist2 < button_radius * button_radius:
                current_fill = button
                break

        if self.last_fill:
            pygame.draw.circle(self.window, (255, 255, 255), self.last_fill[1], button_radius)
            self.last_fill = None
        if current_fill:
            pygame.draw.circle(self.window, (0, 255, 0), current_fill[1], button_radius)
            self.last_fill = current_fill

    def GetMouseBoardPosition(self):
        if self.last_fill:
            return self.last_fill[0]
        else:
            return None