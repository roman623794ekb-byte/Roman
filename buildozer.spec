[app]

# (str) Название вашей игры на экране телефона
title = Tic Tac Toe Pygame

# (str) Имя пакета (только английские буквы, без пробелов)
package.name = tictactoe_pygame

# (str) Домен пакета (уникальный идентификатор приложения)
package.domain = org.demotazh

# (str) Папка с исходным кодом (точка означает текущую директорию)
source.dir = .

# (list) Расширения файлов, которые будут упакованы в APK (добавлены звуки и шрифты)
source.include_exts = py,png,jpg,wav,mp3,ttf,otf

# (str) Версия приложения
version = 1.0.0

# (list) Зависимости приложения.
# ВАЖНО: Вместо kivy здесь указан pygame
requirements = python3, pygame

# (str) Точка входа для Pygame (обязательный параметр для сборки Pygame на Android)
android.entrypoint = org.kivy.android.PythonActivity

# (str) Ориентация экрана (portrait — вертикальная, landscape — горизонтальная)
orientation = portrait

# -----------------------------------------------------------------------------
# Настройки для Android
# -----------------------------------------------------------------------------

# (bool) Полноэкранный режим (1 = скрыть статус-бар сверху, 0 = оставить)
fullscreen = 1

# (int) Минимальная поддерживаемая версия Android (21 = Android 5.0+)
android.minapi = 21

# (list) Разрешения для Android (если игра будет отправлять запросы в сеть, раскомментируйте)
# android.permissions = INTERNET
