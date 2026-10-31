import numpy as np
import pygame


class SoundManager:
    def __init__(self):
        if not pygame.mixer.get_init():
            pygame.mixer.init(frequency=22050, size=-16, channels=1, buffer=512)

        self.sample_rate = 22050

        # Генерация только игровых звуковых эффектов
        self.click_sound = self._create_synth_sound(type="click")
        self.ai_sound = self._create_synth_sound(type="ai")
        self.win_sound = self._create_synth_sound(type="win")
        self.lose_sound = self._create_synth_sound(type="lose")

    def _create_synth_sound(self, type="click"):
        """Синтез игровых эффектов с помощью NumPy"""
        if type == "click":
            duration = 0.08
            t = np.linspace(0, duration, int(self.sample_rate * duration), False)
            frequency = 600 - t * 2000
            wave = np.sin(2 * np.pi * frequency * t) * np.exp(-t * 40)

        elif type == "ai":
            duration = 0.1
            t = np.linspace(0, duration, int(self.sample_rate * duration), False)
            frequency = 320 - t * 400
            wave = (np.sin(2 * np.pi * frequency * t) > 0.0).astype(float) * 0.4
            wave *= np.exp(-t * 20)

        elif type == "win":
            duration = 0.5
            t = np.linspace(0, duration, int(self.sample_rate * duration), False)
            num_samples = len(t)
            freqs = np.zeros(num_samples)
            freqs[:num_samples // 4] = 523.25
            freqs[num_samples // 4:num_samples // 2] = 659.25
            freqs[num_samples // 2:3 * num_samples // 4] = 783.99
            freqs[3 * num_samples // 4:] = 1046.50
            wave = np.sin(2 * np.pi * freqs * t) * (1.0 - t / duration)

        elif type == "lose":
            duration = 0.6
            t = np.linspace(0, duration, int(self.sample_rate * duration), False)
            frequency = 280 - (t ** 2) * 300
            wave = np.sin(2 * np.pi * frequency * t) * np.exp(-t * 4)

        audio_data = np.int16(wave * 32767 * 0.5)
        return pygame.mixer.Sound(buffer=audio_data)

    def play_click(self):
        self.click_sound.play()

    def play_ai(self):
        self.ai_sound.play()

    def play_win(self):
        self.win_sound.play()

    def play_lose(self):
        self.lose_sound.play()
