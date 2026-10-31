import random
import numpy as np
from .base_ai import BaseAI

class RandomAI(BaseAI):
    def get_move(self, board: np.ndarray) -> tuple[int, int]:
        available_moves = list(zip(*np.where(board == 0)))
        return random.choice(available_moves) if available_moves else (0, 0)
