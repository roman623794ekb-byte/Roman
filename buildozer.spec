[app]
title = Cyber Tic Tac Toe
package.name = cybertictactoe
package.domain = org.demotazh
source.dir = .
source.include_exts = py,png,jpg,wav,mp3,ttf
version = 0.1

# Используем официальные рецепты pygame и numpy
requirements = python3,pygame,numpy

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a
android.minapi = 21
android.targetapi = 33
android.copy_libs = 1

[buildozer]
log_level = 2
warn_on_root = 1
