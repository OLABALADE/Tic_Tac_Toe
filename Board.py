import pygame
from constant import *
import numpy as np

class Board:
    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))
        self.empty_sqrs = self.squares
        self.marked_squares = 0


    def terminal_state(self, *screen, show= False):

        #Vertical Win
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                if show:

                    colour = CIR_COLOUR if self.squares[0][col] == 2 else CROSS_COLOUR
                    start = (col * SQSIZE + SQSIZE // 2, 20)
                    end = (col * SQSIZE + SQSIZE // 2, HEIGHT - 20)
                    pygame.draw.line(screen[0], colour, start, end, LINEWIDTH)

                return self.squares[0][col]
            
        #Horizontal win 
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:

                if show:

                    colour = CIR_COLOUR if self.squares[row][0] == 2 else CROSS_COLOUR
                    start = (20, row * SQSIZE + SQSIZE // 2)
                    end = (WIDTH - 20, row * SQSIZE + SQSIZE // 2)
                    pygame.draw.line(screen[0], colour, start, end, LINEWIDTH)

                return self.squares[row][0]
            
        #Descending diagonal win 
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:

            if show:

                colour = CIR_COLOUR if self.squares[0][0] == 2 else CROSS_COLOUR
                start = (20, 20)
                end = (WIDTH - 20, HEIGHT - 20)
                pygame.draw.line(screen[0], colour, start, end, LINEWIDTH)

            return self.squares[1][1]
        
        #Ascending diagonal win 
        if self.squares[0][2] == self.squares[1][1] == self.squares[2][0] != 0:

            if show:

                colour = CIR_COLOUR if self.squares[1][1] == 2 else CROSS_COLOUR
                start = (20, HEIGHT - 20)
                end = (WIDTH - 20, 20) 
                pygame.draw.line(screen[0], colour, start, end, LINEWIDTH)

            return self.squares[1][1]
        
        return 0
    


    def get_empty_squares(self):
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_square(row, col):
                    empty_sqrs.append((row, col))
        return empty_sqrs

    def isempty(self):
        return self.marked_squares == 9

    def mark_square(self, row, col, player):
        self.squares[row][col] = player
        self.marked_squares += 1

    def empty_square(self, row, col):
        return self.squares[row][col] == 0