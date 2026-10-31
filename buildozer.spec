[app]
# (string) Название вашей игры на экране телефона
title = Cyber Tic Tac Toe

# (string) Техническое имя пакета (строчные латинские буквы, без пробелов)
package.name = cybertictactoe

# (string) Уникальный домен организации (без пробелов)
package.domain = org.demotazh

# (string) Директория с исходным кодом (точка означает текущую папку)
source.dir = .

# (list) Расширения файлов, которые будут упакованы внутрь приложения
source.include_exts = py,png,jpg,wav,mp3,ttf

# (string) Версия приложения
version = 0.1

# (list) Критически важные зависимости приложения для Android
requirements = python3,pygame,numpy

# (string) Ориентация экрана (фиксируем вертикальный режим под нашу нижнюю панель)
orientation = portrait

# (bool) Флаг полноэкранного режима (убирает шторку уведомлений Android сверху)
fullscreen = 1

# (list) Разрешения Android (для работы звукового микшера Pygame)
android.permissions = INTERNET, VIBRATE

# (list) Архитектуры процессоров современных смартфонов
android.archs = arm64-v8a, armeabi-v7a

# (string) Минимальная поддерживаемая версия Android API (Android 8.0+)
android.minapi = 26

# (int) Целевая версия Android API (Android 14)
android.targetapi = 34

# (bool) Копировать библиотеки в приватную папку приложения
android.copy_libs = 1

[buildozer]
# (int) Уровень логирования (2 — выводить максимум информации)
log_level = 2

# (int) Предупреждать, если сборка запущена от root-пользователя
warn_on_root = 1
