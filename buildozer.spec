[app]
title = Tic Tac Toe Pygame
package.name = tictactoepygame
package.domain = org.demotazh
source.dir = .
source.include_exts = py,png,jpg,wav,mp3,ttf,otf
version = 1.0.0

# Фиксируем стабильную версию Python (3.11), с которой совместим Pygame
requirements = python3==3.11.9,pygame

android.entrypoint = org.kivy.android.PythonActivity
orientation = portrait
fullscreen = 1
android.minapi = 21
android.api = 33
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
