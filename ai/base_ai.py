from abc import ABC, abstractmethod
import numpy as np

class BaseAI(ABC):
    def __init__(self, ai_player_num: int = 2):
        self.ai_num = ai_player_num
        self.human_num = 3 - ai_player_num

    @abstractmethod
    def get_move(self, board: np.ndarray) -> tuple[int, int]:
        """Должен возвращать кортеж (row, col)"""
        pass
