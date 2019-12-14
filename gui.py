import math
import pygame


def DrawText(string, size, pos):
    """"""
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
            pygame.draw.circle(self.window, (255, 255, 255), pos1, button_radius)
            pygame.draw.circle(self.window, (255, 255, 255), pos2, button_radius)

    def _DrawPieces(self):
        print(self.board.board.tolist())
        for row in range(9):
            for col in range(len(self.board.board[row])):
                color = self.board.board[row][col]
                if color:
                    pr = int(self.height / 24)
                    row_size = (row - 4) * (self.height * math.sqrt(3) / 16)
                    col_size = -(col - 4) * self.height / 8 - abs(row - 4) * (self.height / 16)
                    size = int(row_size + self.size_x), int(col_size + self.size_y)
                    if color == 1:
                        pygame.draw.circle(self.window, (255, 255, 255), size, pr, 1)
                        pygame.draw.circle(self.window, (0, 0, 0), size, pr - 1)
                    elif color == 2:
                        pygame.draw.circle(self.window, (0, 0, 0), size, pr, 1)
                        pygame.draw.circle(self.window, (255, 255, 255), size, pr - 1)
