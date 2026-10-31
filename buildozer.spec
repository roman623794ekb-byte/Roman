# (str) Название вашей игры на экране телефона
title = Tic Tac Toe Pygame

# (str) Имя пакета (Строго маленькие латинские буквы, БЕЗ нижних подчеркиваний)
package.name = tictactoepygame

# (str) Домен пакета (уникальный идентификатор приложения)
package.domain = org.demotazh

# (str) Папка с исходным кодом (точка означает текущую директорию)
source.dir = .

# (list) Расширения файлов, которые будут упакованы в APK (скрипты, графика, звуки, шрифты)
source.include_exts = py,png,jpg,wav,mp3,ttf,otf

# (str) Версия приложения
version = 1.0.0

# (list) Зависимости приложения. Для Pygame на Android пишется строго без пробелов
requirements = python3,pygame

# (str) Точка входа для Pygame (обязательный параметр для запуска на Android)
android.entrypoint = org.kivy.android.PythonActivity

# (str) Ориентация экрана (portrait — вертикальная, landscape — горизонтальная)
orientation = portrait

# (bool) Полноэкранный режим (1 = скрыть статус-бар сверху, 0 = оставить)
fullscreen = 1

# (int) Минимальная поддерживаемая версия Android (21 = Android 5.0+)
android.minapi = 21

# (int) Целевая версия Android API (по умолчанию 34 для современных систем)
android.api = 34

# (str) Архитектура процессора. arm64-v8a обязательна для всех современных смартфонов
android.archs = arm64-v8a

# (bool) Разрешить сборку подтяжкой необходимых библиотек (True)
android.accept_sdk_license = True
