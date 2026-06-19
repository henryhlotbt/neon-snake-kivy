[app]

title = Neon Snake
package.name = neonsnake
package.domain = org.henry

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy

orientation = landscape
fullscreen = 0

# ---------- ANDROID SETTINGS ----------
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

android.archs = arm64-v8a

android.allow_backup = True

# Permissions (safe default for games)
android.permissions = VIBRATE

# ---------- BUILD SETTINGS ----------
p4a.bootstrap = sdl2

log_level = 2
warn_on_root = 1