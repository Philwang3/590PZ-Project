import pygame
import board
import gui
import random
import time

pygame.init()


class AI:

    def __init__(self):
        self.game = board.board()
        self.window = pygame.display.set_mode((700, 600))
        self.play_board = gui.playboard(self.game, self.window)
        self.state = 1
        self.player = None
        self.ai = None
        self.player_choose()
        self.Draw(1)

    def player_choose(self):
        self.player = input("Entering AI game, player choose your color please (b or w): ")
        if self.player == 'b':
            self.ai = 'w'
        elif self.player == 'w':
            self.ai = 'b'
        else:
            print('Sorry, Please do that again')
            self.player_choose()

    def Draw(self, b):
        surface = pygame.display.get_surface()
        surface.fill((0, 0, 0))
        if b == 'over' and self.state == 3:
            if self.game.white_piece == 0:
                text = "Game is Over, Black wins!"
            else:
                text = "Game is Over, White wins!"
            gui.DrawText(text, 45, (150, 150))
        elif self.game.gameover() == False:
            if b == 1:
                text = "Black chess's turn"
            else:
                text = "White chess's turn"
            gui.DrawText(text, 45, (150, 150))
            self.play_board.Draw_board()
            print("PLaying")
        pygame.display.flip()

    def generate_pos(self, player):
        loc = random.randint(0, 23)
        self.game.board[self.game.side[loc][0]][self.game.side[loc][1]] = player
        if player == 1:
            self.game.black_piece = self.game.black_piece - 1
        if player == 2:
            self.game.white_piece = self.game.white_piece - 1

    def generate_direction(self):
        for i in self.game.side:
            if self.game.board[i[0]][i[1]] != 0:
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
            d = random.randint(0,1)
            print(d)
            if d == 0:
                direction = 'L'
            else:
                direction = 'R'

        return direction

    def AI_turn(self):
        if self.ai == 'b':
            block_ai = 1
            b = 2
        elif self.ai == 'w':
            block_ai = 2
            b = 1
        self.generate_pos(block_ai)
        print(block_ai)
        direction = self.generate_direction()
        print("direction" + direction)
        self.game.push(direction)
        self.game.update()
        print("AI's turn:")
        time.sleep(2)
        self.Draw(b)

    def player_turn(self):
        if self.player == 'b':
            block_player = 1
            b = 2
        elif self.player == 'w':
            block_player = 2
            b = 1
        self.game.insert(block_player)
        direction = self.game.direction()
        self.game.push(direction)
        self.game.update()
        self.Draw(b)

    def run(self):
        n = 1
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:  # 判断事件类型是否为退出事件
                pygame.quit()
                return
            elif self.game.gameover() == False:
                self.state = 2
                if n % 2 != 0:
                    if self.ai == 'b':
                        self.AI_turn()
                    elif self.ai == 'w':
                        self.player_turn()
                else:
                    if self.ai == 'b':
                        self.player_turn()
                    elif self.ai == 'w':
                        self.AI_turn()
                n = n + 1
                print(self.game.board.tolist())
            elif self.game.gameover() == True:
                self.state = 3
                self.Draw('over')
                return


if __name__ == "__main__":
    game = AI()
    game.run()

