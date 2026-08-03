import pygame
from constant import *
from Board import *
from AI import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def show_screen():
    pygame.display.set_caption("Tic Tac Toe")
    screen.fill(BG_COLOUR)


class Game:

    def __init__(self):
        self.display_lines()
        self.board = Board()
        self.ai = AI()
        self.player = 1
        self.running = True
        self.gamemode = "ai"
        



    def display_lines(self):
        screen.fill(BG_COLOUR)
        #Vertical lines
        pygame.draw.line(screen, LINESCOLOUR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINEWIDTH)
        pygame.draw.line(screen, LINESCOLOUR, (WIDTH - SQSIZE, 0), (WIDTH - SQSIZE, HEIGHT), LINEWIDTH)

        #Horizontal lines
        pygame.draw.line(screen, LINESCOLOUR, (0, SQSIZE), (WIDTH, SQSIZE), LINEWIDTH)
        pygame.draw.line(screen, LINESCOLOUR, (0, HEIGHT - SQSIZE), (WIDTH, HEIGHT - SQSIZE), LINEWIDTH) 


    def next_turn(self):
        self.player = self.player % 2 + 1

    def render_player(self, row, col):
        if self.player == 1:
            #Descending line
            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            pygame.draw.line(screen, CROSS_COLOUR, start_desc, end_desc, CROSS_WIDTH)

            #Ascending line
            start_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
            end_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            pygame.draw.line(screen, CROSS_COLOUR, start_asc, end_asc, CROSS_WIDTH)


        if self.player == 2:
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
            pygame.draw.circle(screen, CIR_COLOUR, center, RADIUS, CIR_WIDTH)

    def make_move(self, board, row, col):
        board.mark_square(row, col, self.player)
        self.render_player(row, col)
        self.next_turn()

    def change_gamemode(self):
        self.gamemode = "ai" if self.gamemode == "pvp" else "pvp"

    def reset(self):
        self.__init__()


    def is_over(self):
        return self.board.isempty() or self.board.terminal_state(screen, show=True) != 0
