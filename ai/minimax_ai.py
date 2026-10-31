import numpy as np
from .base_ai import BaseAI


class MinimaxAI(BaseAI):
    def get_move(self, board: np.ndarray) -> tuple[int, int]:
        best_score = float('-inf')
        best_move = None

        # Перебор всех возможных ходов
        for row in range(3):
            for col in range(3):
                if board[row, col] == 0:
                    board[row, col] = self.ai_num
                    score = self.minimax(board, 0, False)
                    board[row, col] = 0
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        return best_move

    def _check_winner(self, board: np.ndarray):
        for p in [self.ai_num, self.human_num]:
            for i in range(3):
                if np.all(board[i, :] == p) or np.all(board[:, i] == p): return p
            if np.all(np.diag(board) == p) or np.all(np.diag(np.fliplr(board)) == p): return p
        if not np.any(board == 0): return 0
        return None

    def minimax(self, board: np.ndarray, depth: int, is_maximizing: bool) -> int:
        winner = self._check_winner(board)
        if winner == self.ai_num: return 10 - depth
        if winner == self.human_num: return depth - 10
        if winner == 0: return 0

        if is_maximizing:
            best_score = float('-inf')
            for r in range(3):
                for c in range(3):
                    if board[r, c] == 0:
                        board[r, c] = self.ai_num
                        score = self.minimax(board, depth + 1, False)
                        board[r, c] = 0
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for r in range(3):
                for c in range(3):
                    if board[r, c] == 0:
                        board[r, c] = self.human_num
                        score = self.minimax(board, depth + 1, True)
                        board[r, c] = 0
                        best_score = min(score, best_score)
            return best_score
