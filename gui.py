import math
import pygame


def DrawText(string, size, pos):
    """For plotting text message and chess board using PyGame framework, we looked into the gui.py
    of  https://github.com/piotrf17/gipf and learnt some of its plotting method, so we learnt that and modified some
    of the usage to fit our own code."""
    surface = pygame.display.get_surface()
    font = pygame.font.Font(None, size)
    text = font.render(string, 1, (255, 255, 255))
    position = text.get_rect()
    position.topleft = pos
    surface.blit(text, position)

class playboard(object):

    def __init__(self, board, window):
        self.board = board
        self.window = window
        x, y = self.window.get_size()
        self.size_x = 0.6 * x
        self.size_y = 0.6 * y
        self.height = 0.8 * 0.6 * y

    def Draw_board(self):
        print("running Draw Board")
        self.DrawLine(0)
        self.DrawLine(math.pi / 3)
        self.DrawLine(-math.pi / 3)
        self._DrawPieces()

    def DrawLine(self, angle):
        """This step is to print all the lines in the chess board, we wish to print 8 lines with an given angle"""
        button_radius = int(self.height / 48)
        for i in range(1, 8):
            row_size = (i - 4) * (self.height * math.sqrt(3) / 16)
            col_size = self.height / 2 - abs(i - 4) * (self.height / 16)
            sin = math.sin(angle)
            cos = math.cos(angle)
            pos1 = [cos * row_size - sin * (-col_size), sin * row_size + cos * (-col_size)]
            pos2 = [cos * row_size - sin * col_size, sin * row_size + cos * col_size]
            pos1[0] = int(pos1[0] + self.size_x)
            pos2[0] = int(pos2[0] + self.size_x)
            pos1[1] = int(pos1[1] + self.size_y)
            pos2[1] = int(pos2[1] + self.size_y)

            pygame.draw.line(self.window, (255, 255, 255), pos1, pos2)
            if angle == math.pi / 3:
                if i == 1:
                   DrawText(str(9), 15, [pos1[0]+3, pos1[1]+3])
                if i == 2:
                   DrawText(str(10), 15, [pos1[0]+3, pos1[1]+3])
                if i == 3:
                   DrawText(str(11), 15, [pos1[0]+3, pos1[1]+3])
                if i == 4:
                   DrawText(str(12), 15, [pos1[0]+3, pos1[1]+3])
                   DrawText(str(0), 15, [pos2[0]+3, pos2[1]+3])
                if i == 5:
                   DrawText(str(23), 15, [pos2[0]+3, pos2[1]+3])
                if i == 6:
                   DrawText(str(22), 15, [pos2[0]+3, pos2[1]+3])
                if i == 7:
                   DrawText(str(21), 15, [pos2[0]+3, pos2[1]+3])
            if angle == -math.pi / 3:
                if i == 1:
                   DrawText(str(1), 15, [pos1[0]+3, pos1[1]+3])
                if i == 2:
                   DrawText(str(2), 15, [pos1[0]+3, pos1[1]+3])
                if i == 3:
                   DrawText(str(3), 15, [pos1[0]+3, pos1[1]+3])
                if i == 4:
                   DrawText(str(4), 15, [pos1[0]+3, pos1[1]+3])
                   DrawText(str(16), 15, [pos2[0]+3, pos2[1]+3])
                if i == 5:
                   DrawText(str(15), 15, [pos2[0]+3, pos2[1]+3])
                if i == 6:
                   DrawText(str(14), 15, [pos2[0]+3, pos2[1]+3])
                if i == 7:
                   DrawText(str(13), 15, [pos2[0]+3, pos2[1]+3])
            if angle == 0:
                if i == 1:
                   DrawText(str(5), 15, [pos1[0]+3, pos1[1]+3])
                if i == 2:
                   DrawText(str(6), 15, [pos1[0]+3, pos1[1]+3])
                if i == 3:
                   DrawText(str(7), 15, [pos1[0]+3, pos1[1]+3])
                if i == 4:
                   DrawText(str(8), 15, [pos1[0]+3, pos1[1]+3])
                   DrawText(str(20), 15, [pos2[0]+3, pos2[1]+3])
                if i == 5:
                   DrawText(str(19), 15, [pos2[0]+3, pos2[1]+3])
                if i == 6:
                   DrawText(str(18), 15, [pos2[0]+3, pos2[1]+3])
                if i == 7:
                   DrawText(str(17), 15, [pos2[0]+3, pos2[1]+3])
            pygame.draw.circle(self.window, (255, 255, 255), pos1, button_radius)
            pygame.draw.circle(self.window, (255, 255, 255), pos2, button_radius)

    def _DrawPieces(self):
        """This step is to update the chess position after the chess board gets updated, it generally check the
        list we stored in our board class and print all the chess position after movement"""
        print(self.board.board.tolist())
        for row in range(9):
            for col in range(len(self.board.board[row])):
                color = self.board.board[row][col]
                if color:
                    pr = int(self.height / 24)
                    row_pos = (row - 4) * (self.height * math.sqrt(3) / 16)
                    col_pos = -(col - 4) * self.height / 8 - abs(row - 4) * (self.height / 16)
                    pos = int(row_pos + self.size_x), int(col_pos + self.size_y)
                    if color == 1:
                        pygame.draw.circle(self.window, (255, 255, 255), pos, pr, 1)
                        pygame.draw.circle(self.window, (0, 0, 0), pos, pr - 1)
                    elif color == 2:
                        pygame.draw.circle(self.window, (0, 0, 0), pos, pr, 1)
                        pygame.draw.circle(self.window, (255, 255, 255), pos, pr - 1)
