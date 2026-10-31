import numpy as np

class TicTacToeGame:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1  # 1 - Человек (X), 2 - ИИ (O)
        self.winner = None
        self.game_over = False
        self.win_line = None  # Хранит кортеж: ('row'/'col'/'diag', индекс)

    def make_move(self, row: int, col: int) -> bool:
        if self.board[row, col] == 0 and not self.game_over:
            self.board[row, col] = self.current_player
            self.check_status()
            if not self.game_over:
                self.current_player = 3 - self.current_player
            return True
        return False

    def check_status(self):
        # Проверка строк и столбцов
        for i in range(3):
            if np.all(self.board[i, :] == self.current_player):
                self.winner = self.current_player
                self.game_over = True
                self.win_line = ('row', i)
                return
            if np.all(self.board[:, i] == self.current_player):
                self.winner = self.current_player
                self.game_over = True
                self.win_line = ('col', i)
                return

        # Проверка главной диагонали (сверху-слева вниз-справа)
        if np.all(np.diag(self.board) == self.current_player):
            self.winner = self.current_player
            self.game_over = True
            self.win_line = ('diag', 0)
            return

        # Проверка побочной диагонали (снизу-слева вверх-справа)
        if np.all(np.diag(np.fliplr(self.board)) == self.current_player):
            self.winner = self.current_player
            self.game_over = True
            self.win_line = ('diag', 1)
            return

        # Проверка на ничью
        if not np.any(self.board == 0):
            self.winner = 0  # Ничья
            self.game_over = True
            self.win_line = None

    def reset(self):
        self.board.fill(0)
        self.current_player = 1
        self.winner = None
        self.game_over = False
        self.win_line = None
