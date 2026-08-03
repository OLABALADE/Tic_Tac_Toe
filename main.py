import pygame
from game import *
from constant import *
import sys

pygame.init()
show_screen()



def main():
    game = Game()
    ai = game.ai
    board = game.board

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE
                if board.empty_square(row, col) and game.running:
                    game.make_move(board, row, col)
                    if game.is_over():
                        game.running = False

 
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_c:
                    game.change_gamemode()

                if event.key == pygame.K_r:
                    game.reset()
                    board = game.board
                    ai = game.ai

                if event.key == pygame.K_0:
                    ai.level = 0
                
                if event.key == pygame.K_1:
                    ai.level = 1


        if game.gamemode == "ai" and game.player == ai.player and game.running:
            pygame.display.update()

            row,col = ai.evaluate(board)
            game.make_move(board, row, col)
            if game.is_over():
                game.running = False


        pygame.display.update()

            
main()