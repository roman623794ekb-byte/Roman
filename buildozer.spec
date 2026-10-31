title = Ticaoegame
package.name = tictactoepygame
package.domain = org.demotazh
source.dir = .
source.include_exts = py,png,jpg,wav,mp3,ttf,otf
version = 1.0.0
requirements = python3,pygame
android.entrypoint = org.kivy.android.PythonActivity
orientation = portrait
fullscreen = 1
android.minapi = 21
android.api = 33
android.archs = arm64-v8a
android.accept_sdk_license = True

# Фиксируем стабильную версию NDK, чтобы избежать конфликтов компилятора C++
android.ndk = 26b
