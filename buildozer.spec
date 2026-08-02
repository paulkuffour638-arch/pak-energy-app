[app]
title = PAK Energy Tech Hub
package.name = pakenergy
package.domain = org.paulkuffour
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt
version = 1.0

requirements = python3,kivy,fpdf2

orientation = portrait
fullscreen = 0
icon.filename = %(source.dir)s/pak_logo.png

android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 34
android.minapi = 24
android.ndk = 28c
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 0
