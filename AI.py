from copy import deepcopy
from random import choice


class AI:

    def __init__(self, level=1, player=2):
        self.level = level
        self.player = player
        self.best_move = ()

    def random_square(self, board):
        empty_squares = board.get_empty_squares()
        rnd_square = choice(empty_squares)
        return rnd_square

    def mini_max(self, board, alpha, beta, maximizing):
        if maximizing:
            print("X turn")
        else:
            print("O turn")
        print(board.squares, "\n")

        if board.terminal_state() == 1:
            return [1, ()]

        elif board.terminal_state() == 2:
            return [-1, ()]

        elif board.isempty():
            return [0, ()]

        if maximizing:

            max_eval, max_eval_sqr = [-10000, ()]
            empty_squares = board.get_empty_squares()

            for square in empty_squares:

                new_board = deepcopy(board)
                row, col = square

                new_board.mark_square(row, col, 1)

                eval_max, eval_sqr_max = self.mini_max(
                    new_board, alpha, beta, False)

                if eval_max > max_eval:
                    max_eval_sqr = square
                    max_eval = eval_max

                # Alpha-Beta Pruning
                alpha = max(alpha, max_eval)
                if beta <= alpha:
                    break

            return [max_eval, max_eval_sqr]

        else:

            mini_eval, min_eval_sqr = [10000, ()]
            empty_squares = board.get_empty_squares()

            for square in empty_squares:

                new_board = deepcopy(board)
                row, col = square

                new_board.mark_square(row, col, 2)

                eval_min, eval_sqr_min = self.mini_max(
                    new_board, alpha, beta, True)

                if eval_min < mini_eval:
                    min_eval_sqr = square
                    mini_eval = eval_min

                # Alpha-Beta Pruning
                beta = min(beta, mini_eval)
                if beta <= alpha:
                    break

            return [mini_eval, min_eval_sqr]

    def evaluate(self, main_board):
        if self.level == 0:
            move = self.random_square(main_board)

        else:
            board = deepcopy(main_board)

            eval, self.best_move = self.mini_max(board, -10000, 10000, False)
            move = self.best_move

        return move
